"""
This document just shows the process of turning the British Social Attitudes Survey into a csv suited for two-group analysis and the graph generation software.

Author: Joey Cartwright
Date: 20-07-2024
"""

import numpy as np
import pandas as pd

def load_and_transform():  
    """
    Loads the 2021 BSA and transforms certain variables such that they lend themselves well to two-group analysis. Also removes answers such as 'Prefer Not to Say' and 'Don't Know' and, if the user chose a 10-option question,, ensures that 8 and 9 are not removed.

    Raises:
    KeyError: if issue_var can't be found in the Data Frame

    Returns: 
    data: The transformed and cleaned data Set

    Raises: 
    FileNotFoundError: If the 2021 BSA isn't in the folder specified
    ParserError: If there is an issue parsing the file

    """
    file_path = r"C:\Users\Joeys\Documents\Python\Polarisation_Project\BSA 2021\UKDA-9072-tab\tab\bsa21_archive.tab"
    try:
        data = pd.read_csv(file_path, sep = '\t')
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at {file_path} could not be found.")
    except pd.errors.ParserError:
        raise pd.errors.ParserError(f"Error: The file could not be parsed")

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

    ten_set = ["MiEcono", "MiCultur", "TrstLgl", "TrstPlc", "HltSat", "IntPriv", "IntMidi"]
    replace_values = [-1, 998, 999, 77, 88, 98, 99]
    extra_values = [8, 9]
    
    for col in data.columns:
        if col in ten_set:
            data[col] = data[col].replace(replace_values, np.nan)
        else:
            data[col] = data[col].replace(replace_values + extra_values, np.nan)

    data.to_csv(r"C:\Users\Joeys\Documents\Python\Polarisation_Project\political_wedges\server\my_project\data\bsa_data.csv", index=False)

    return data

if __name__ == "__main__":
    load_and_transform()