""""
This module turns the 'Polarisation Parallelogram', a statistical and visual framework I developed during my MA in Quantitative Politics, into an full graph generation tool.
This particular module is designed to be part of the backend for a website, and so by defaut imports the 2021 British Social Attitudes Survey, the focus of the website. As a result, it is 
primarily tailored to creating the visualisations and associated data. Other versions of this module will more resemble a classical statistical package.

Author: Joey Cartwright
Date: 20/07/2024
"""

# Data Preparation

# Global Constants
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import statsmodels.api as sm


list_of_topics = ["Finance and Economics", "Workplaces", "Housing and Urban Development", "Gender and Sexual Minorities", 
                "British Values and Traditions", "Welfare", "Law and Order", "Governance", "Health and Social Care", "Class", "Miscellaneous"]

list_of_scales = [['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree'],
            ['Support Strongly', 'Support', 'Neither/It Depends', 'Oppose', 'Oppose Strongly'],
            ['Strongly \nin Favour', 'Somewhat \nin Favour', 'Neither', 'Somewhat Against', 'Strongly Against'],
            ["1 - Not at All British", "2", "3", "4", "5", "6", "7 - Very British"], 
            ["0 - \n Extremely Dissatisfied", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \nExtremely Satisfied"], 
            ["0 \n (Not at All)", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 \n (Completely)"], 
            ["Always Wrong", "Mostly Wrong", "Sometimes Wrong/\nIt Depends", "Rarely Wrong", "Not Wrong at All"],
            ["Gone much too far", "Gone too far", "About right", "Not gone \nfar enough", "Not gone \n nearly far enough"],
            ["0 - \n Extremely Bad", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \n Extremely Good"],
            ["0 - \n Undermines", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \n Enriches"],
            ["Very important", "Quite important", "Not very \nimportant", "Not at all \nimportant"],
            ["Very wide", "Fairly wide", "Not very wide", "No difference*"],
            ["Very difficult", "Fairly difficult", "Not very difficult"],
            ["Greater differences", "About the same", "Less differences"],
            ["Spend much more", "Spend more", "Spend the same \n as now", "Spend less", "Spend much less"]]

colour_dic = {
    'AgeGroup': {
        1: ('olivedrab', "18-34"),
        2: ('goldenrod', "35-54"),
        3: ('grey', "55+")
    },
    'partyfw': {
        1: ('blue', "Conservative \nLean"),
        2: ('red', "Labour Lean"),
        3: ('orange', "Lib Dem Lean"),
        4: ('yellow', "SNP Lean"),
        5: ('teal', "Plaid Cymru Lean"),
        6: ('green', "Green Party \nLean"),
        7: ('purple', "UKIP Lean"),
        8: ('aqua', "Reform Party \nLean")
    },
    'HigherEd': {
        1: ('navy', "Degree"),
        2: ('gold', "No Degree")
    },
    'SRInc': {
        1: ('gold', "Identify as \nHigh Income"),
        2: ('grey', "Identify as \nMiddle Income"),
        3: ('brown', "Identify as \nLow Income")
    },
    'DVSex21': {
        1: ('lightseagreen', "Female"),
        2: ('maroon', "Male")
    },
    'RaceOri4': {
        1: ('brown', "Black"),
        2: ('goldenrod', "Asian"),
        3: ('white', "White"),
        4: ('tan', "Mixed")
    },
    'Religion': {
        1: ('red', "Non-Religious"),
        2: ('orange', "Christian"),
        3: ('yellow', "Buddhist"),
        4: ('green', "Hindu"),
        5: ('darkturquoise', "Jewish"),
        6: ('navy', "Muslim"),
        7: ('magenta', "Sikh"),
        8: ('sienna', "Other Religion")
    }
}

# Question name: (Variable name, scale index, topic index)
questions_dict = {
    "Would you like to see more or less government spending on [benefits for unemployed people] than now?*": ("SOCSPND1", 14, 5),
    "Would you like to see more or less government spending on [benefits for disabled people who cannot work] than now?*": ("SOCSPND2", 14, 5),
    "Would you like to see more or less government spending on [benefits for parents who work on very low incomes] than now?*": ("SOCSPND3", 14, 5),
    "Would you like to see more or less government spending on [single parents] than now?*": ("SOCSPND4", 14, 5),
    "Would you like to see more or less government spending on [retired people] than now?*": ("SOCSPND5", 14, 5),
    "Would you like to see more or less government spending on [carers for those who are sick or disabled] than now?*": ("SOCSPND6", 14, 5),
    "How wide are the differences between social classes in this country, do you think?": ("DWSocCL", 11, 10),
    "How difficult would you say it is for people to move from one class to another?": ("ClassMov", 12, 10),
    "Do you think [social class] differences have become greater or less or have remained about the same?*": ("DCSocCL", 13, 10),
    "Have attempts to give people with physical impairments an equal chance in the workplace gone too far or not far enough?": ("EqOpDis", 7, 1),
    "Have attempts to give people with mental health conditions an equal chance in the workplace gone too far or not far enough?": ("EqOpMh", 7, 1),
    "If a man and woman have sexual relations before marriage, what would your general opinion be?": ("PMS", 6, 3),
    "Opinions on sexual relations between two adults of the same sex": ("HomoSex", 6, 3),
    "Do you think attempts to give equal opportunities have gone too far or not gone far enough for LGB people?*": ("EQOPPGAY", 7, 1),
    "Do you think attempts to give equal opportunities have gone too far or not gone far enough for transgender people?*": ("EQOPPT", 7, 1),
    "Do you think attempts to give equal opportunities have gone too far or not gone far enough for women?*": ("CHOPWOMM", 7, 1),
    "Do you think attempts to give equal opportunities have gone too far or not gone far enough for black and asian people?*": ("EQOPPBLK", 7, 1),
    "How important do you think being born in britain is for being truly british?*": ("PATRIOT1", 10, 4),
    "How important do you think having british ancestry is for being truly british?*": ("PATRIOT8", 10, 4),
    "How important do you think feeling british is for being truly british?*": ("PATRIOT7", 10, 4),
    "Would you say it is generally bad or good for Britain's economy that migrants come to Britain from other countries?": ("MiEcono", 8, 0),
    "Would you say that Britain's cultural life is generally undermined or enriched by migrants coming to live here from other countries?": ("MiCultur", 9, 0),
    "On a score of 0-10 how much do you personally trust Britain's legal system?*": ("TrstLgl", 5, 7),
    "On a score of 0-10 how much do you personally trust Britain's Police*": ("TrstPlc", 5, 7),
    "Please say what you think overall about the state of health services in Britain nowadays": ("HltSat", 4, 8),
    "To what extent would you say that online and mobile communication undermines personal privacy?": ("IntPriv", 5, 9),
    "To what extent would you say that online and mobile communication exposes people to misinformation?": ("IntMisi", 5, 9),
    "'Now that Scotland has its own parliament, Scottish MP’s should no longer be allowed to vote in the House of commons on laws that only affect England'": ("WestLoth", 0, 7),
    "'Overall, it is worthwhile for me to save into a private pension'": ("PrPSvWW", 0, 0),
    "How strongly do you agree or disagree that, in principle, someone who has been off work with a back problem going back to work quickly will help speed their recovery?*": ("PhsRecov", 0, 1),
    "How strongly do you agree or disagree that, in principle, someone who has been off work with depression going back to work quickly will help speed their recovery?*": ("MntRecov", 0, 1),
    "Would you support or oppose more homes being built in your local area?": ("HomsBult", 1, 2),
    "To what extent would you support or oppose requiring people in existing buildings to make changes to their homes to meet new energy regulations, should new homes be built in that area?*": ("RegUpd", 1, 2),
    "To what extent are you in favour of, or against, new cycle lanes in roads being introduced in your area?*": ("Cyclne", 2, 2),
    "To what extent are you in favour of, or against, your local council spending more money to improve existing public transport, although this may mean spending less on other council services?*": ("LclTrn", 2, 2),
    "To what extent are you in favour of, or against, reserving parking spaces for electric car charging points being introduced in your area?*": ("ElecPrk", 2, 2),
    "To what extent are you in favour of, or against, building carparks to introduce more “park and ride” routes being introduced in your area?*": ("BldPrk", 2, 2),
    "To what extent are you in favour of, or against, narrowing roads to widen pavements being introduced in your area?*": ("NrwPv", 2, 2),
    "To what extent are you in favour of, or against, closing roads to create pedestrian high streets being introduced in your area?*": ("ClsRd", 2, 2),
    "On a scale of 1 to 7, with 1 being ‘not at all British’, and 7 ‘being very strongly British’, to what extent do you think of yourself as British?": ("BritID2", 3, 4),
    "'The world would be a better place if people from other countries were more like the British'": ("Natlike", 0, 4),
    "Generally speaking, Britain is a better country than most other countries": ("NatBest", 0, 4),
    "How much do you agree or disagree that a person who is transgender should be able to have the sex recorded on their birth certificate changed if they want?": ("TBirCert", 0, 3),
    "'Around here, most unemployed people could find a job if they really wanted one'": ("UnempJob", 0, 5),
    "'Many people who get social security don't really deserve any help'": ("SocHelp", 0, 5),
    "'Most people on the dole are fiddling in one way or another'": ("DoleFidl", 0, 5),
    "'If welfare benefits weren't so generous, people would learn to stand on their own two feet'": ("WelfFeet", 0, 5),
    "'The welfare state encourages people to stop helping each other'": ("welfhelp", 0, 5),
    "'The government should spend more money on welfare benefits for the poor, even if it leads to higher taxes'": ("morewelf", 0, 5),
    "'Cutting welfare benefits would damage too many people's lives'": ("damlives", 0, 5),
    "'The creation of the welfare state is one of Britain's proudest achievements'": ("proudwlf", 0, 5),
    "'Government should redistribute income from the better-off to those who are less well off'": ("Redistrb", 0, 0),
    "'Big business benefits owners at the expense of workers'": ("BigBusnN", 0, 0),
    "'Ordinary working people do not get their fair share of the nation's wealth'": ("Wealth", 0, 0),
    "'There is one law for the rich and one for the poor'": ("RichLaw", 0, 0),
    "'Management will always try to get the better of employees if it gets the chance'": ("Indust4", 0, 0),
    "'Young people today don't have enough respect for traditional British values'": ("TradVals", 0, 4),
    "'People who break the law should be given stiffer sentences'": ("StifSent", 0, 6),
    "'For some crimes, the death penalty is the most appropriate sentence'": ("DeathApp", 0, 6),
    "'Schools should teach children to obey authority'": ("Obey", 0, 6),
    "'The law should always be obeyed, even if a particular law is wrong'": ("WrongLaw", 0, 6),
    "'Censorship of films and magazines is necessary to uphold moral standards'": ("Censor", 0, 6)
}

def load():
    file_path = r"C:\Users\Joeys\Documents\Python\Polarisation_Project\political_wedges\server\my_project\data\bsa_data.csv"
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {file_path} could not be found.")
    except pd.errors.ParserError:
        raise pd.errors.ParserError(f"Error: The file could not be parsed")
    
    data = data.fillna(0)
    data = data.astype(int)
    return data

# Creates the group arrays
def group_arrays(group_var, group_1_value, group_2_value, issue_var):
    """
    Creates arrays of the list of values in each set of responses for easy access

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user

    Returns: 
    arr_1, arr_2: The two group arrays

    """
    frame = load()
    arr_1 = frame[frame[group_var] == group_1_value][issue_var].values
    arr_2 = frame[frame[group_var] == group_2_value][issue_var].values

    arr_1 = arr_1[arr_1 != 0]
    arr_2 = arr_2[arr_2 != 0]
    print(arr_1)

    return arr_1, arr_2

# Creates the cumulative distribution array
def dist_creator(group_var, group_var_value, issue_var):
    """
    Creates the distributions of answers - both standard and cumulative - for the parallelogram function and associated table

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user

    Returns:
    G_cum: The cumulative distribution of answers for both groups
    G_sorted_rounded: The standard rounded distribution of answers for the table.

    Raises:
    ValueError: If there are no responses (i.e. n = 0)

    """

    frame = load()
    group_data = frame[frame[group_var] == group_var_value][issue_var]

    group_data = group_data[group_data != 0]

    G_counts = group_data.value_counts()

    if G_counts.empty:
        raise ValueError("No responses found")
    
    # Creates the cumulative percentages
    G_prop = (G_counts/sum(G_counts)) * 100
    G_prop[0] = 0
    G_sorted = G_prop.sort_index()
    G_cum = G_sorted.cumsum()
    G_sorted_rounded = G_sorted.round(2)
    return G_cum, G_sorted_rounded



def missing(ser1, ser2, labs=False, cum=True):
    """
    Deals with cases where certain categories have no answers (e.g. nobody answered 'Strongly Agree') by filling in with either 0 (in the standard distribution case) or the previous percentage
    number (in the cumulative distribution case)
    
    Parameters: 
    ser1: Series of Group 1, either standard or cumulative
    ser1: Series of Group 2, either standard or cumulative

    Returns:
    missing_fixed: both series, now with the missing answers filled in

    Raises:
    TypeError: If ser1 or ser2 is not a pandas Series

    """
    if not isinstance(ser1, pd.Series) or not isinstance(ser2, pd.Series):
        raise TypeError("Both ser1 and ser2 should be pandas Series")
    
    # Infers missing number(s) within scale
    def gap_fill(ser):
        for i in range(ser.index[0], ser.index[-1]):
            if i not in ser.index:
                if cum:
                    ser.loc[i] = ser.loc[i - 1]
                else:
                    ser.loc[i] = 0
            ser.sort_index(inplace=True)
        return ser
    
    ser1 = gap_fill(ser1)
    ser2 = gap_fill(ser2)

    # Adds hypothetical value at the end if an extreme case is missing
    def end_cases(ser1, ser2):
        while ser1.index[-1] > ser2.index[-1]:
            new_key = ser2.index[-1] + 1
            if cum:
                new_value = ser2.iloc[-1]
            else:
                new_value = 0
                print(new_value*100)
            ser2.loc[new_key] = new_value
        
        while ser2.index[-1] > ser1.index[-1]:
            new_key = ser1.index[-1] + 1
            if cum:
                new_value = ser1.iloc[-1]
            else:
                new_value = 0
                print(new_value*100)
            ser1.loc[new_key] = new_value
        return (ser1, ser2)

    missing_fixed = end_cases(ser1, ser2)

    # Adds 'Floor' at the beginning to ensure lines meet at both ends, and adds extra values if a scale is specified that does not match the distribution of answers.
    def label_check(ser1, ser2, labs):
        if labs:
            if labs[0] != 'Floor':
                labs.insert(0, 'Floor')
            while len(labs) > len(ser1):
                new_key = ser1.index[-1] + 1
                if cum:
                    new_value = ser1.iloc[-1]
                else:
                    new_value = 0
                    print(new_value*100)
                ser1.loc[new_key] = new_value

                new_key = ser2.index[-1] + 1
                if cum:
                    new_value = ser2.iloc[-1]
                else:
                    new_value = 0
                    print(new_value*100)
                ser2.loc[new_key] = new_value
        return ser1, ser2
    
    missing_fixed = label_check(ser1, ser2, labs)

    if not cum:
        print(missing_fixed)
    return missing_fixed

def table_cols(array_1, array_2, name_1, name_2, scale):
    """
    Creates the columns of the table of answers

    Parameters: 
    array_1: The distribution of answers for Group 1
    array_2: The distribution of answers for Group 2
    name_1 (str): The name of Group 1
    name_2 (str): The name of Group 2
    scale (ls): The list of possible answers for that question

    Returns:
    table_data: The table data in the form of three columns

    Raises: 
    TypeError: If group names are not strings
    ValueError: If columns are not the same length

    """
    title_1 = "Answer"
    array_1_copy = array_1.copy()
    array_2_copy = array_2.copy()
    array_1_copy = array_1_copy.tolist()
    array_2_copy = array_2_copy.tolist()
    array_1_copy = [f"{value}%" for value in array_1_copy]
    array_2_copy = [f"{value}%" for value in array_2_copy]
    array_3_copy = scale.copy()

    if not isinstance(name_1, str) or not isinstance(name_2, str):
        raise TypeError("Names of Groups should be strings")
    
    array_1_copy[0] = name_1
    array_2_copy[0] = name_2
    array_3_copy[0] = title_1

    if not (len(array_1_copy) == len(array_2_copy) == len(array_3_copy)):
        raise ValueError("Columns of table should all be the same length")

    table_data = list(zip(array_3_copy, array_1_copy, array_2_copy))
    table_data.insert(0, ("", "Matrix", ""))
    return table_data
    

def cores(group_var, value_1, value_2, issue_var):
    """
    Creates the 'statistically relevant' parts of the distribution - i.e. with the ends excluded, as these will always be 0% and 100%. Predominantly useful for the lambda statistical test, but also
    forms part of the parallelogram

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    issue_var: The variable corresponding to the question specified by the end user


    Returns:
    y1_core, y2_core: The distributions minus the ends

    """
    y1 = dist_creator(group_var, value_1, issue_var)[0]
    y2 = dist_creator(group_var, value_2, issue_var)[0]
    missing_check = missing(y1, y2)
    y1_core, y2_core = missing_check[0][1:-1], missing_check[1][1:-1]
    return y1_core, y2_core

# Statistical Analysis Functions

def pol_lambda(group_var, group_1_value, group_2_value, issue_var):
    """
    Creates the figure measuring the percentage of opinion divergence between the two groups. Parameters are specified again since this can be used as a standalone function as well as part of the main
    parallelogram function
    
    Parameters:
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    issue_var: The variable corresponding to the question specified by the end user

    Returns:
    ld (float): The value of lambda

    Raises: 
    ValueError: If lambda is less than zero or above one hundred

    """
    core_1, core_2 = cores(group_var, group_1_value, group_2_value, issue_var)
    diff = abs(core_1 - core_2)
    ld = (sum(diff)/(len(diff)))

    if ld < 0 or ld > 100:
        raise ValueError(f"Lambda is {ld:.2f}, but should not be below zero or above one hundred by definition")
    return ld

# Tests the statistical significance of lamda
def lambda_test(group_var, group_1_value, group_2_value, issue_var):
    """
    Statistical test for the significance of lambda. This happens to be equivalent to a difference in means test in most cases, which can be shown mathematically (see PDF on website for more detail)
    Once again, parameters specified so test can be done as a standalone function

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    issue_var: The variable corresponding to the question specified by the end user

    Returns:
    p_value: The p-value of the statistical test
    sig: The number of asterisks to be included in the graph, based on level of significance
    len(arrays[0]), len(arrays[1]): The sample sizes of each group

    Raises:
    ValueError: If the p-value is less than zero or greater than one
    TypeError: If the p-value is not a float

    """
    arrays = group_arrays(group_var, group_1_value, group_2_value, issue_var)
    p_value = sm.stats.ttest_ind(arrays[0], arrays[1])[1]

    if p_value < 0 or p_value > 1:
        raise ValueError("The p-value is {p_value:.2f} but it should be between zero and one")
    if not isinstance(p_value, float):
        raise TypeError("p-value should be a float")
    
    sig = ""
    if p_value < 0.05:
        sig += "*"
    if p_value < 0.01:
        sig += "*"
    if p_value < 0.001:
        sig += "*"
    return (p_value, sig, len(arrays[0]), len(arrays[1]))

# Creates the figure measuring the extremity of the opinions of each group relative to a mean of neutrality
def pol_epsilons(group_var, group_1_value, group_2_value, issue_var):
    """
    Creates the figure measuring each group's extremity, between -100% and 100%

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    issue_var: The variable corresponding to the question specified by the end user

    Returns:
    ep1, ep2: The values of extremity for each group

    Raises: 
    ValueError: If ep1 or ep2 are either less than -100 or more than 100

    """
    core_1, core_2 = cores(group_var, group_1_value, group_2_value, issue_var)
    core_length = len(cores(group_var, group_1_value, group_2_value, issue_var)[0])

    ep1 = (2 * (sum(core_1)/(core_length)) - 100)
    ep2 = (100 - 2 * (sum(core_2)/(core_length)))

    if ep1 < -100 or ep1 > 100 or ep2 < -100 or ep2 > 100:
        raise ValueError("Epsilons should be between zero and 100")

    return ep1, ep2

def get_pol_level(ld):
    """
    Assigns each lambda value to 'extreme', 'high', 'moderate' or 'low'

    Parameters: 
    ld (float): The value of lambda
    
    Returns:
    pol: The corresponding word depending on the lambda value

    Raises: 
    TypeError: if lambda is not a number

    """
    try:
        if ld >= 40:
            pol = 'extreme'
        elif ld >= 25:
            pol = 'high'
        elif ld >= 10:
            pol = 'moderate'
        else:
            pol = 'low'
    except TypeError:
        raise TypeError("Lambda should be a number")
    return pol

# Helper Functions for Aesthetics of Parallelogram


def get_colour(group_var, group_1_value, group_2_value, colour_dic):
    """
    Searches for the colour that should be assigned to the line of each group (e.g. Green for Green Party)
    
    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    colour_dic (dict): A dictionary that maps groups to colours

    Returns:
    col_1, col_2: The colours of each line
    label_1, label_": The corresponding labels for each group

    Raises: 
    KeyError: if colours or labels could not be found
    
    """
    try:
        col_1, col_2 = colour_dic[group_var][group_1_value][0], colour_dic[group_var][group_2_value][0]
    except KeyError:
        raise KeyError("At least one colour could not be found")
    
    try:
        label_1, label_2 = colour_dic[group_var][group_1_value][1], colour_dic[group_var][group_2_value][1]
    except KeyError:
        raise KeyError("At least one label could not be found")

    return (col_1, col_2, label_1, label_2)

def fill_in(y1, y2, ld):
    """
    Creates the areas to be filled in and colour to be assigned to the wedge based on the value of lambda, where a larger lambda means a redder center
    
    Parameters: 
    y1: The list of values for group 1
    y2: The list of values for group 2
    ld: The value of lambda

    Returns:
    fill: The area of the wedge itself
    fill_b1, fill_b2: The areas to be filled on either side of the wedge
    col: The colour of the wedge

    Raises: 
    Exception: If unexpected error occurs
    
    """

    #Identifies wedge vertices
    try:
        vertices = []
        y1_rev = y1[::-1]
        b1, b2 = [], []
        for i, val2 in y2.items():
            vertices.append((i, val2))
            b2.append((i, val2))
        for i, val1 in y1.items():
            b1.append((i, val1))
        for j, val1 in y1_rev.items():
            vertices.append((j, val1))
        b1.append((1,100))
        b2.append((len(y1)-2, 0))
        ld_norm = ld / 100

        # Creates wedge colour based on level of polarisation
        r = min(10 * ld_norm, 1)
        g = 1 - min(ld_norm * 4, 1)
        color = (r,g,0)
        
        # Fills in wedge and parallelogram
        fill = patches.Polygon(vertices, closed=True, facecolor = color, alpha = 0.5, linewidth = 0)
        fill_b1 = patches.Polygon(b1, closed=True, facecolor = 'black', alpha = 0.3, linewidth = 0)
        fill_b2 = patches.Polygon(b2, closed=True, facecolor = 'black', alpha = 0.3, linewidth = 0)
    except Exception as e:
        print(f"Unexpected error: {e}")

    return fill, fill_b1, fill_b2, color

def lambda_positioning(leng, ld_x_value, y1, y2):
    """
    Determines whether lambda can fit inside the wedge. If it cannot, it appears outside with a line pointing to the center of the wedge.
    
    Parameters: 
    leng (int): The number of possible answers in the scale
    ld_x_value: Lambda's x position, by default in the center portion of the graph
    y1: The list of values for group 1
    y2: The list of values for group 2

    Returns:
    (ld_x_value, ld_y_value) (tup): x and y coordinates for lambda

    Raises: 

    """

    if not isinstance(leng, int) or leng <= 0:
        raise ValueError(f"leng is {leng} but should be a positive integer")

    if leng % 2 == 0:
        ref = leng/2
        mean_a = np.mean([y1[ref], y2[ref]])
        mean_b = np.mean([y1[ref - 1], y2[ref - 1]])
        graph_mean = np.mean([mean_a, mean_b])
        ld_y_value = graph_mean
        top_left = (ref - 0.9, graph_mean + 1)
        bottom_right = (ref - 0.1, graph_mean - 4)
        y1_check = (ref - 0.9, (9 * y1[ref - 1] + y1[ref]) / 10)
        y2_check = (ref - 0.1, (y2[ref - 1] + 9 * y2[ref]) / 10)

        if top_left[1] > y1_check[1] or bottom_right[1] < y2_check[1]:
            ld_x_value = ref
            ld_y_value = ld_y_value - 10
            text_offset = 3
            plt.plot([ld_x_value, 0.5 * (leng - 1)], [ld_y_value + text_offset, graph_mean], color='black', linestyle='-', linewidth=1)
        else:
            ld_y_value = graph_mean

    else:
        ref = (leng - 1)/2
        graph_mean = np.mean([y1[ref], y2[ref]])
        ld_y_value = graph_mean
        top_left = (ref - 0.4, graph_mean + 1)
        bottom_right = (ref + 0.4, graph_mean - 4)
        y1_check = (ref - 0.4, (3 * y1[ref - 1] + 7 * y1[ref]) / 10)
        y2_check = (ref + 0.4, (7 * y2[ref] + 3 * y2[ref + 1]) / 10)
        if top_left[1] > y1_check[1] or bottom_right[1] < y2_check[1]:
            ld_x_value = ref + 0.5
            ld_y_value = ld_y_value - 10
            text_offset = 3
            plt.plot([ld_x_value, 0.5 * (leng - 1)], [ld_y_value + text_offset, graph_mean], color='black', linestyle='-', linewidth=1)
        else:
            ld_y_value = graph_mean

    if ld_y_value < 6:
        ld_y_value = -2

    return (ld_x_value, ld_y_value)


def parallelogram(group_var, group_1_value, group_2_value, question):
    """
    Creates the actual parallelogram visually, along with the associated statistical data

    Parameters: 
    group_var: The demographic being studied
    group_1_value: The first group within that demographic specified by end user
    group_2_value: The second group within that demographic specified by end user
    question (str): The survey question specified by the end user

    Returns:
    plt: The plot of the parallelogram and associated data

    Raises:
    KeyError: If there is an issue with dictionary lookups for the scale or the question variable
    ValueError: If the length of the scale specified and the number of options do not match


    """
    try:
        issue_var = questions_dict[question][0]
    except KeyError:
        raise KeyError(f"'{question}' could not be found in the dictionary")
    
    try:
        custom_labels = list_of_scales[questions_dict[question][1]]
    except KeyError:
        raise KeyError(f"The scale for '{question}' could not be found in the dictionary")


    # Gets the cumulative distributions
    y1, array_1 = dist_creator(group_var, group_1_value, issue_var)
    y2, array_2 = dist_creator(group_var, group_2_value, issue_var)

    # Checks for missing categories
    missing_check = missing(y1, y2, labs = custom_labels)
    y1, y2 = missing_check

    missing_check_for_table = missing(array_1, array_2, labs = custom_labels, cum=False)
    array_1, array_2 = missing_check_for_table

    # Colours
    colour_G1, colour_G2, label_1, label_2 = get_colour(group_var, group_1_value, group_2_value, colour_dic)
    group_1_name = label_1
    group_2_name = label_2

    # Ensures that 'Group 1' is always the higher group
    if np.mean(y1) < np.mean(y2):
        y1, y2 = y2, y1
        array_1, array_2 = array_2, array_1
        group_1_value, group_2_value = group_2_value, group_1_value
        group_1_name, group_2_name = group_2_name, group_1_name
        colour_G1, colour_G2 = colour_G2, colour_G1
    leng = len(y1)


    table_data = table_cols(array_1, array_2, group_1_name, group_2_name, custom_labels)
    print(table_data)


    # Test statistical significance 
    sig_test = lambda_test(group_var, group_1_value, group_2_value, issue_var)
    n_1 = sig_test[2]
    n_2 = sig_test[3]

    # Builds and adds components of the graph that are not depending on the numerical data
    plt.style.use('seaborn')
    plt.figure(figsize=(12,6), facecolor="#b0e0e6")
    plt.gca().set_facecolor("#b0e0e6")
    plt.title(question, fontsize = 1200/len(question))
    plt.xlabel("Answer", fontsize = 14)
    plt.ylabel("Cumulative Percentage of Respondents", fontsize = 14)

    # Builds Table

    table = plt.table(cellText=table_data[1:],
                    colLabels=table_data[0],
                    cellLoc='center',
                    loc='center',
                    bbox=[1.3, 0.1, 0.6, 0.9]
                    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)

    for key, cell in table._cells.items():
        if key[0] == 0:
            cell.set_facecolor("#b0e0e6")
            cell.set_text_props(fontsize=14)
            cell.set_edgecolor('none')
        else:
            cell.set_facecolor("#b0e0e6")
            cell.set_linewidth(1)
            cell.set_text_props(fontweight='bold', ha='center', va='center')

    # Calculates lambda
    ld = pol_lambda(group_var, group_1_value, group_2_value, issue_var)
    ld_x_value = 0.5 * (leng-1)

    #Places Lambda Figure
    plt.text(lambda_positioning(leng, ld_x_value, y1, y2)[0], lambda_positioning(leng, ld_x_value, y1, y2)[1], f'\n$\\mathbf{{{round(ld, 2)}\%}}${sig_test[1]}', fontsize=10, color = 'black', ha = 'center', va = 'center')

    # If a list of labels equal to the number of x points on the graph is specified, this adds the labels

    if custom_labels:
        if len(custom_labels) != leng:
            raise ValueError(f"Length of custom_labels {len(custom_labels)} is not the same as alleged number of options {leng}")
        plt.xticks(range(leng), custom_labels, fontsize = 8)
    else:
        plt.xticks(range(leng))

    #Plots the lines of the graph
    plt.plot(y1, 'o' + "-", color = colour_G1, linewidth = 3, label = group_1_name)
    plt.plot(y2, 'o' + "-", color = colour_G2, linewidth = 3, label = group_2_name)
    plt.legend(loc = 'lower right', fontsize = 10, bbox_to_anchor=(1.1, 0.03))

    #Fills in the different parts of the graph
    fill = fill_in(y1, y2, ld)
    plt.gca().add_patch(fill[0])
    plt.gca().add_patch(fill[1])
    plt.gca().add_patch(fill[2])

    # Calculates Epsilons and adds to corner of graph
    epsilon_1, epsilon_2 = pol_epsilons(group_var, group_1_value, group_2_value, issue_var)
    plt.text(-0.2, 99, f'$\lambda$ = {round(ld,2)}%\n$\epsilon_1$ = {round(epsilon_1, 2)}%\n$\epsilon_2$ = {round(epsilon_2, 2)}%', \
    bbox=dict(facecolor='white', alpha=0.5, edgecolor='#f2f2f2', boxstyle='round,pad=0.3'), ha = 'left', va = 'top', fontsize = 8)

    # Small Sample Warning
    if n_1 < 40:   
        plt.text(leng-0.9, 70, f'Small sample \n of {group_1_name} \n respondents ({n_1}) ', \
            bbox=dict(facecolor='red', alpha=0.5, edgecolor='red', boxstyle='round,pad=0.3'), ha = 'left', va = 'center', fontsize = 8)
    if n_2 < 40:   
        plt.text(leng-0.9, 50, f'Small sample \n of {group_2_name} \n respondents ({n_2}) ', \
            bbox=dict(facecolor='red', alpha=0.5, edgecolor='red', boxstyle='round,pad=0.3'), ha = 'left', va = 'center', fontsize = 8)


    pol = get_pol_level(ld)
    plt.text(leng-0.9, 30, f'There is $\\mathbf{{{pol}}}$ \npolarisation on this \nquestion between the \ngroups specified', \
        bbox=dict(facecolor=fill[3], alpha=0.5, boxstyle='round,pad=0.3'), ha = 'left', va = 'center', fontsize = 8)

    # Creates actual parallelogram
    vertices = [(leng - 2 , 0), (leng - 2 + 1, 100), (1, 100), (0, 0)]
    shape = patches.Polygon(vertices, closed=True, edgecolor='black', facecolor = 'none', linestyle='--', linewidth = 1.5)
    plt.gca().add_patch(shape)

    # Amends size to fit extras
    plt.subplots_adjust(right=0.55)
    plt.subplots_adjust(left=0.1)

    plt.savefig('redist.png', dpi=300)

    return plt.show()

# Testing
if __name__ == "__main__":
    parallelogram('Religion', 1, 6, "Would you say that Britain's cultural life is generally undermined or enriched by migrants coming to live here from other countries?")


    















