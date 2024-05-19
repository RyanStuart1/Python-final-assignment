#!/usr/bin/env python

import pandas as pd
import sys

"""
The purpose of this script is to refine the data from the csv 'Scotland_teaching_file_1PCT.csv'.
In short the script: removes duplicates; confirms the data types for each variable; removes rows with null values; 
and lastly checks if the values of variables are within the range of the dataset, if not they will be removed from the refined csv.
"""

def drop_duplicates(df, subset=['Record_Number'], keep=False):
    """
    The drop_duplicates function checks for duplicate record numbers in the DataFrame.
    
    If the boolean returned is "True", the duplicates were removed.

    If the boolean returned is "False", there were no duplicates to be removed.
    """
    original_length = len(df)
    dropped_duplicates = df.drop_duplicates(subset='Record_Number', keep=keep)
    dropped_length = len(dropped_duplicates)
    if original_length != dropped_length:
        print("No Duplicates were found and dropped!!")
        return True
    else:
        print("No Duplicates were found!!")
        return False 

def check_format(df):
    """
    The check_format function reiterates the column dtypes.
    """
    for column in df.columns:
        if df[column].dtype == 'int64':
            print(f"{column}: integer")
        elif df[column].dtype == 'object':
            print(f"{column}: object")
        else:
            print(f"{column}: {df[column].dtype}")         

def remove_null_rows(df):
    """
    If there are any rows containing null values they will be removed from the DataFrame.
    """
    remove_null_rows = df.dropna()
    return df.dropna()


def check_values_of_variables_are_admissible(df):
    """
    The value checker function firstly converts all the columns which are of the object dtype, containing both string and int values to dtype: str.
    After doing so the function will check that the values of variables are within the given range from the "Teaching_File_Variable_List.xlsx" documentation.
    """
    # Columns that need to be converted to string
    str_columns = [
        "Family_Composition", "Economic_Activity", "Occupation",
        "industry", "Hours_Worked_Per_Week", "Approximate_Social_Grade"
    ]
    
    # Convert specified columns to string
    df[str_columns] = df[str_columns].astype(str)

    # Filter conditions for various variables
    df = df[(df["RESIDENCE_TYPE"].isin(['P', 'C']))]
    df = df[(df["Family_Composition"].between("0", "5")) | (df["Family_Composition"] == 'X')]
    df = df[(df["sex"].between(1, 2))]
    df = df[(df["age"].between(1, 8))]
    df = df[(df["Marital_Status"].between(1, 5))]
    df = df[(df["student"].between(1, 2))]
    df = df[(df["Country_Of_Birth"].between(1, 2))]
    df = df[(df["health"].between(1, 5))]
    df = df[(df["Ethnic_Group"].between(1, 6))]
    df = df[(df["religion"].between(1, 9))]
    df = df[df["industry"].isin(['X'] + list(map(str, range(1, 14))))]
    df = df[df["Economic_Activity"].isin(['X'] + list(map(str, range(1, 10))))]
    df = df[df["Occupation"].isin(['X'] + list(map(str, range(1, 10))))]
    df = df[df["Hours_Worked_Per_Week"].isin(['X'] + list(map(str, range(1, 5))))]
    df = df[df["Approximate_Social_Grade"].isin(['X'] + list(map(str, range(1, 5))))]

    return df

if __name__ == '__main__':
    if len(sys.argv) == 2:
        sys.exit(1)
    print("refinedata.py <../data/Scotland_teaching_file_1PCT.csv>")

    input_file = sys.argv[0]
    output_file = '../data/Refined_Scotland_teaching_file_1PCT.csv'

    df = pd.read_csv('../data/Scotland_teaching_file_1PCT.csv')
    
    drop_duplicates(df)
    check_format(df)
    df = remove_null_rows(df)
    df = check_values_of_variables_are_admissible(df)
    
    df.to_csv(output_file, index=False)
    print(f"Refined data saved to {'../data/Refined_Scotland_teaching_file_1PCT.csv'}")