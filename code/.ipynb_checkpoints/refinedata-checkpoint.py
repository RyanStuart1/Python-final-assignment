#!/usr/bin/env python

import pandas as pd

df.read_csv('../data/Scotland_teaching_file_1PCT.csv')

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
        print("No Duplicates were found and dropped")
        return True
    else:
        print("No Duplicates were found")
        return False 
dropped_duplicates = drop_duplicates(df)
print(dropped_duplicates)

def check_format(df):
    """
    The check_format function reiterates the column dtypes
    """
    for column in df.columns:
        if df[column].dtype == 'int64':
            print(f"{column}: integer")
        elif df[column].dtype == 'object':
            print(f"{column}: object")
            
check_format(df)

def remove_null_rows(df):
    """
    If there are any rows containing null values they will be removed from the DataFrame.
    """
    remove_null_rows = df.dropna()
    return df.dropna()
    
remove_null_rows(df)

def check_values_of_variables_are_admissible(df):
    # Convert the string obj dtype values to string
    df["Family_Composition"] = df["Family_Composition"].astype(str)
    df["Economic_Activity"] = df["Economic_Activity"].astype(str)
    df["Occupation"] = df["Occupation"].astype(str)
    df["industry"] = df["industry"].astype(str)
    df["Hours_Worked_Per_Week"] = df["Hours_Worked_Per_Week"].astype(str)
    df["Approximate_Social_Grade"] = df["Approximate_Social_Grade"].astype(str)
   
    """
    The check_values_of_variables_are_admissible function scans over the DataFrame,
    ensuring that the values of variables match the assigned range.
    """
    
    df = df[(df["RESIDENCE_TYPE"].isin(['P','C']))] 
    df = df[(df["Family_Composition"].between("0", "5")) | (df["Family_Composition"] == 'X')]
    df = df[(df["sex"].between(1, 2))]
    df = df[(df["age"].between(1, 8))]
    df = df[(df["Marital_Status"].between(1, 5))]
    df = df[(df["student"].between(1, 2))]
    df = df[(df["Country_Of_Birth"].between(1, 2))]
    df = df[(df["health"].between(1, 5))]
    df = df[(df["Ethnic_Group"].between(1, 6))]
    df = df[(df["religion"].between(1, 9))]
    df = df[(df["Economic_Activity"].between("1", "9")) | (df["Economic_Activity"] == 'X')]
    df = df[(df["Occupation"].between("1", "9")) | (df["Occupation"] == 'X')]
    df = df[(df["industry"].between("1", "13")) | (df["industry"] == 'X')]
    df = df[(df["Hours_Worked_Per_Week"].between("1", "4")) | (df["Hours_Worked_Per_Week"] == 'X')]
    df = df[(df["Approximate_Social_Grade"].between("1", "4")) | (df["Approximate_Social_Grade"] == 'X')]

    return df
check_values_of_variables_are_admissible(df)        
   

df.to_csv('../data/Refined_data_Scotland_teaching_file_1PCT.csv', index=False)

if __name__ == '__main__':

    
