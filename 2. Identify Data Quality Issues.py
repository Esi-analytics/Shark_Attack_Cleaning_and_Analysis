# -*- coding: utf-8 -*-
"""
Created on Fri May 17 04:42:41 2024

@author: esina
"""

"""import Chardet"""
import chardet

"""import pandas"""
import pandas as pd



"""received a utf-8 encoding error. find my data encoding"""
with open(r'C:\Users\esina\OneDrive\Desktop\Rasmussen\Data Quality in Analytics\SharkAttack.csv', 'rb') as file:
    result = chardet.detect(file.read())
    print(result)

"""read file in with the new encoding"""
shk = pd.read_csv(r'C:\Users\esina\OneDrive\Desktop\Rasmussen\Data Quality in Analytics\SharkAttack.csv', dtype = 'str', encoding = 'Windows-1252', delimiter = ',')
 
try:   
    """count missing values"""
    try:
        missing_values = shk.isnull().sum()
        print("missing values per column:\n", missing_values)
    except Exception as error:
        print(f"can not count missing values: {error}")



    """find duplicates"""
    try:
        all_duplicate_rows = shk[shk.duplicated(keep=False)]
        print("All occurrences of duplicate rows:\n", all_duplicate_rows)
    except Exception as error:
        print(f"can not find duplicates: {error}")
        
    """count the number of duplicate rows"""
    try:
        num_duplicates = shk.duplicated().sum()
        print(f"Number of duplicate rows: {num_duplicates}")
    except Exception as error:
        print(f"can not find count duplicate rows: {error}")
        
    try:
        """find inconsistencies in text data"""
        inconsistent_entries = shk['Type'].str.lower().unique()
        print(inconsistent_entries)
    except Exception as error:
            print(f"can not find any inconsistencies: {error}")
        
    finally:
        """checking data stats"""
        print(shk.describe())
        
    try:
        """display basic information about the dataframe"""
        print(shk.info())
    except Exception as error:
        print(f"can not display basic information about the file: {error}")
                
    try:
        """Each column has the correct data type"""
        print(shk.dtypes)
    except Exception as error:
        print(f"data type error: {error}")

finally:      
    """write File"""
    shk.to_excel('sharkoutput.xlsx', index=False)

"""print the output"""
print("output file created succesfully")