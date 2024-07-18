# Data Preparation

# Global Constants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import statsmodels.api as sm


list_of_topics = ["Finance and Economics", "Workplaces", "Housing and Urban Development", "Gender and Sexual Minorities", 
                "British Values and Traditions", "Welfare", "Law and Order", "Governance", "Health and Social Care", "Class", "Miscellaneous"]

list_of_scales = [['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree'],
            ['Support Strongly', 'Support', 'Neither/It Depends', 'Oppose', 'Oppose Strongly'],
            ['Strongly in Favour', 'Somewhat in Favour', 'Neither', 'Somewhat Against', 'Strongly Against'],
            ["1 - Not at All British", "2", "3", "4", "5", "6", "7 - Very British"], 
            ["0 - \n Extremely Dissatisfied", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \n Extremely Satisfied"], 
            ["0 \n (Not at All)", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 \n (Completely)"], 
            ["Always Wrong", "Mostly Wrong", "Sometimes Wrong/\nIt Depends", "Rarely Wrong", "Not Wrong at All"],
            ["Gone much too far", "Gone too far", "About right", "Not gone far enough", "Not gone \n nearly far enough"],
            ["0 - \n Extremely Bad", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \n Extremely Good"],
            ["0 - \n Undermines", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 - \n Enriches"],
            ["Very important", "Quite important", "Not very important", "Not at all important"],
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
        1: ('blue', "Conservative Lean"),
        2: ('red', "Labour Lean"),
        3: ('orange', "Lib Dem Lean"),
        4: ('yellow', "SNP Lean"),
        5: ('teal', "Plaid Cymru Lean"),
        6: ('green', "Green Party Lean"),
        7: ('purple', "UKIP Lean"),
        8: ('aqua', "Reform Party Lean")
    },
    'HigherEd': {
        1: ('navy', "Degree"),
        2: ('gold', "No Degree")
    },
    'SRInc': {
        1: ('gold', "Identify as High Income"),
        2: ('grey', "Identify as Middle Income"),
        3: ('brown', "Identify as Low Income")
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
    #"Would you like to see more or less government spending on [benefits for unemployed people] than now?*": ("SOCSPND1", 14, 5),
    #"Would you like to see more or less government spending on [benefits for disabled people who cannot work] than now?*": ("SOCSPND2", 14, 5),
    #"Would you like to see more or less government spending on [benefits for parents who work on very low incomes] than now?*": ("SOCSPND3", 14, 5),
    #"Would you like to see more or less government spending on [single parents] than now?*": ("SOCSPND4", 14, 5),
    #"Would you like to see more or less government spending on [retired people] than now?*": ("SOCSPND5", 14, 5),
    #"Would you like to see more or less government spending on [carers for those who are sick or disabled] than now?*": ("SOCSPND6", 14, 5),
    #"How wide are the differences between social classes in this country, do you think?": ("DWSocCL", 11, 10),
    #"How difficult would you say it is for people to move from one class to another?": ("ClassMov", 12, 10),
    #"Do you think [social class] differences have become greater or less or have remained about the same?*": ("DCSocCL", 13, 10),
    "Have attempts to give people with physical impairments an equal chance in the workplace gone too far or not far enough?": ("EqOpDis", 7, 1),
    "Have attempts to give people with mental health conditions an equal chance in the workplace gone too far or not far enough?": ("EqOpMh", 7, 1),
    "If a man and woman have sexual relations before marriage, what would your general opinion be?": ("PMS", 6, 3),
    "Opinions on sexual relations between two adults of the same sex": ("HomoSex", 6, 3),
    #"Do you think attempts to give equal opportunities have gone too far or not gone far enough for LGB people?*": ("EQOPPGAY", 6, 1),
    #"Do you think attempts to give equal opportunities have gone too far or not gone far enough for transgender people?*": ("EQOPPT", 6, 1),
    #"Do you think attempts to give equal opportunities have gone too far or not gone far enough for women?*": ("CHOPWOMM", 6, 1),
    #"Do you think attempts to give equal opportunities have gone too far or not gone far enough for black and asian people?*": ("EQOPPBLK", 6, 1),
    #"How important do you think being born in britain is for being truly british?*": ("PATRIOT1", 10, 4),
    #"How important do you think having british ancestry is for being truly british?*": ("PATRIOT8", 10, 4),
    #"How important do you think feeling british is for being truly british?*": ("PATRIOT7", 10, 4),
    #"Would you say it is generally bad or good for Britain's economy that migrants come to Britain from other countries?": ("MiEcono", 8, 0),
    #"Would you say that Britain's cultural life is generally undermined or enriched by migrants coming to live here from other countries?": ("MiCultur", 9, 0),
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



def load_and_transform():
    
    # Imports the 2021 BSA and prepares data
    file_path = r"C:\Users\Joeys\Documents\Python\Polarisation_Project\BSA 2021\UKDA-9072-tab\tab\bsa21_archive.tab"
    data = pd.read_csv(file_path, sep = '\t')
    data['AgeGroup'] = data['RespAge_Archive']
    data['AgeGroup'] = pd.cut(data['AgeGroup'], bins = [18, 34, 55, 124], labels = [1,2,3], right = False)
    education_dic = {1: 1, 2: 2, 3: 2, 4: 2}
    data['HigherEd'] = data['hedqual2']
    data['HigherEd'] = data['HigherEd'].map(education_dic)
    religion_dic = {1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3, 9: 4, 10: 5, 11: 6, 12: 7, 13: 8, 20: 2}
    data['Religion'] = data['relrfw_Archive']
    data['Religion'] = data['Religion'].map(religion_dic)
    data.loc[data['PMS'] == 6, 'PMS'] = 3
    data.loc[data['HomoSex'] == 6, 'HomoSex'] = 3
    data.loc[data['HomsBult'] == 6, 'HomsBult'] = 3

    return data


# Removes missing values
def mv_removal(issue_var):
    frame = load_and_transform()
    ten_set = ["MiEcono", "MiCultur", "TrstLgl", "TrstPlc", "HltSat", "IntPriv", "IntMidi"]
    frame = frame[~frame[issue_var].isin([-1, 998, 999, 77, 88, 98, 99])]
    if issue_var not in ten_set:
        frame = frame[~frame[issue_var].isin([8,9])]
    return frame


# Creates the group arrays
def group_arrays(group_var, group_1_value, group_2_value, issue_var):
    frame = mv_removal(issue_var)
    arr_1 = frame[frame[group_var] == group_1_value][issue_var].values
    arr_2 = frame[frame[group_var] == group_2_value][issue_var].values
    return arr_1, arr_2

# Creates the cumulative distribution array
def cum_creator(group_var, group_var_value, issue_var):
    # Drops 'Don't Know' and 'Prefer Not To Answer'
    frame = mv_removal(issue_var)
    G_counts = frame[frame[group_var] == group_var_value][issue_var].value_counts()

    # Adds the floor
    G_counts[0] = 0

    # Creates the cumulative percentages
    G_prop = (G_counts/sum(G_counts)) * 100
    G_cum = G_prop.sort_index().cumsum()
    return G_cum

# Deals with situations where one category has no answers
def missing(ser1, ser2, labs=False):

    # Infers missing number(s) within scale
    def gap_fill(ser):
        for i in range(ser.index[0], ser.index[-1]):
            if i not in ser.index:
                ser.loc[i] = ser.loc[i - 1]
            ser.sort_index(inplace=True)
        return ser
    
    ser1 = gap_fill(ser1)
    ser2 = gap_fill(ser2)

    # Adds hypothetical value at the end if an extreme case is missing
    def end_cases(ser1, ser2):
        while ser1.index[-1] > ser2.index[-1]:
            new_key = ser2.index[-1] + 1
            new_value = ser2.iloc[-1]
            ser2.loc[new_key] = new_value
        
        while ser2.index[-1] > ser1.index[-1]:
            new_key = ser1.index[-1] + 1
            new_value = ser1.iloc[-1]
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
                new_value = ser1.iloc[-1]
                ser1.loc[new_key] = new_value

                new_key = ser2.index[-1] + 1
                new_value = ser2.iloc[-1]
                ser2.loc[new_key] = new_value
        return ser1, ser2
    
    missing_fixed = label_check(ser1, ser2, labs)

    return missing_fixed

# Creates the 'relevant' parts of the distribution - i.e. with the ends excluded, as these will always be 0% and 100%
def cores(group_var, value_1, value_2, issue_var):
    y1, y2 = cum_creator(group_var, value_1, issue_var), cum_creator(group_var, value_2, issue_var)
    missing_check = missing(y1, y2)
    y1_core, y2_core = missing_check[0][1:-1], missing_check[1][1:-1]
    return y1_core, y2_core

# Statistical Analysis Functions

# Creates the figure measuring the percentage of opinion divergence between the two groups
def pol_lambda(group_var, group_1_value, group_2_value, issue_var):
    core_1, core_2 = cores(group_var, group_1_value, group_2_value, issue_var)
    diff = abs(core_1 - core_2)
    ld = (sum(diff)/(len(diff)))
    return ld

# Tests the statistical significance of lamda
def lambda_test(group_var, group_1_value, group_2_value, issue_var):
    arrays = group_arrays(group_var, group_1_value, group_2_value, issue_var)
    p_value = sm.stats.ttest_ind(arrays[0], arrays[1])[1]
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
    core_1, core_2 = cores(group_var, group_1_value, group_2_value, issue_var)
    core_length = len(cores(group_var, group_1_value, group_2_value, issue_var)[0])
    ep1 = (2 * (sum(core_1)/(core_length)) - 100)
    ep2 = (100 - 2 * (sum(core_2)/(core_length)))
    return ep1, ep2

def get_pol_level(ld):
    if ld >= 40:
        pol = 'extreme'
    elif ld >= 25:
        pol = 'high'
    elif ld >= 10:
        pol = 'moderate'
    else:
        pol = 'low'
    return pol

# Helper Functions for Aesthetics of Parallelogram


def get_colour(group_var, group_1_value, group_2_value, colour_dic):
    col_1, col_2 = colour_dic[group_var][group_1_value][0], colour_dic[group_var][group_2_value][0]
    label_1, label_2 = colour_dic[group_var][group_1_value][1], colour_dic[group_var][group_2_value][1]
    return (col_1, col_2, label_1, label_2)

def fill_in(y1, y2, ld):

    #Identifies wedge vertices
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
    return fill, fill_b1, fill_b2, color

def lambda_positioning(leng, ld_x_value, y1, y2):
    if leng % 2 == 0:
        ref = leng/2
        mean_a = np.mean([y1[ref], y2[ref]])
        mean_b = np.mean([y1[ref - 1], y2[ref - 1]])
        graph_mean = np.mean([mean_a, mean_b])
        ld_y_value = graph_mean
        if False:
            vertices_2 = [(ref - 0.9, graph_mean - 4), (ref - 0.1, graph_mean - 4), (ref - 0.1, graph_mean + 1), (ref - 0.9, graph_mean + 1)]
            limit_box = patches.Polygon(vertices_2, closed=True, edgecolor='black', facecolor = 'none', linestyle='--', linewidth = 1.5)
            plt.gca().add_patch(limit_box)

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



# Creates the main visualisation of polarisation and extremity
def parallelogram(group_var, group_1_value, group_2_value, question):

    issue_var = questions_dict[question][0]
    custom_labels = list_of_scales[questions_dict[question][1]]

    # Gets the cumulative distributions
    y1 = cum_creator(group_var, group_1_value, issue_var)
    y2 = cum_creator(group_var, group_2_value, issue_var)

    # Checks for missing categories
    missing_check = missing(y1, y2, labs = custom_labels)
    y1, y2 = missing_check

    # Colours
    colour_G1, colour_G2, label_1, label_2 = get_colour(group_var, group_1_value, group_2_value, colour_dic)
    group_1_name = label_1
    group_2_name = label_2

    # Ensures that 'Group 1' is always the higher group
    if np.mean(y1) < np.mean(y2):
        y1, y2 = y2, y1
        group_1_value, group_2_value = group_2_value, group_1_value
        group_1_name, group_2_name = group_2_name, group_1_name
        colour_G1, colour_G2 = colour_G2, colour_G1
    leng = len(y1)

    # Test statistical significance 
    sig_test = lambda_test(group_var, group_1_value, group_2_value, issue_var)
    n_1 = sig_test[2]
    n_2 = sig_test[3]

    # Builds and adds components of the graph that are not depending on the numerical data
    plt.style.use('seaborn')
    plt.figure(facecolor="#b0e0e6")
    plt.gca().set_facecolor("#b0e0e6")
    plt.title(question, fontsize = 1200/len(question))
    plt.xlabel("Answer", fontsize = 14)
    plt.ylabel("Cumulative Percentage of Respondents", fontsize = 14)

    # Calculates lambda
    ld = pol_lambda(group_var, group_1_value, group_2_value, issue_var)
    ld_x_value = 0.5 * (leng-1)

    #Places Lambda Figure
    plt.text(lambda_positioning(leng, ld_x_value, y1, y2)[0], lambda_positioning(leng, ld_x_value, y1, y2)[1], f'\n$\\mathbf{{{round(ld, 2)}\%}}${sig_test[1]}', fontsize=10, color = 'black', ha = 'center', va = 'center')

    # If a list of labels equal to the number of x points on the graph is specified, this adds the labels
    if custom_labels:
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
    if n_1 < 20 or n_2 < 20:
        print(f"WARNING: For one or more of the groups you have chosen, the sample size is very small and thus the graph is unlikely to represent the actual distribution of opinions for that group. Are you sure you would like to view the graph anyway?")

    pol = get_pol_level(ld)
    plt.text(leng-0.9, 30, f'There is $\\mathbf{{{pol}}}$ \npolarisation on this \nquestion between the \ngroups specified', \
        bbox=dict(facecolor=fill[3], alpha=0.5, boxstyle='round,pad=0.3'), ha = 'left', va = 'center', fontsize = 8)

    #Creates actual parallelogram
    vertices = [(leng - 2 , 0), (leng - 2 + 1, 100), (1, 100), (0, 0)]
    shape = patches.Polygon(vertices, closed=True, edgecolor='black', facecolor = 'none', linestyle='--', linewidth = 1.5)
    plt.gca().add_patch(shape)

    #Amends size to fit extras
    plt.subplots_adjust(right=0.85)
    plt.subplots_adjust(left=0.15)

    return plt.show()

# Testing
if __name__ == "__main__":
    parallelogram('SRInc', 1, 3, "'Ordinary working people do not get their fair share of the nation's wealth'")


    















