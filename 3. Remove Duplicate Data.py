# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:47:32 2024

@author: esina
"""
"""WK 3 directions: Read the file using Python libraries, Identify duplicate records, Remove all the duplicate records, Write the output into new file"""
"""import pandas"""
import pandas as pd


"""read file in with the new encoding"""
shk = pd.read_csv(r'C:\Users\esina\OneDrive\Desktop\Rasmussen\Data Quality in Analytics\SharkAttack.csv', dtype = 'str', encoding = 'Windows-1252', delimiter = ',')

try:
    try:
        """find duplicates"""
        all_duplicate_rows = shk[shk.duplicated(keep=False)]
        print("All occurrences of duplicate rows:\n", all_duplicate_rows)
    except Exception as error:
        print(f"can not find duplicates: {error}")
    
    try:
        """count the number of duplicate rows"""
        num_duplicates = shk.duplicated().sum()
        print(f"Number of duplicate rows: {num_duplicates}")
    except Exception as error:
        print(f"cannot count the number of duplicate rows: {error}")
      
    try:
        "remove all duplicate rows"
        shk_unique = shk.drop_duplicates()
        print("\nshk afer removing duplicates:")
        print(shk_unique)
    except Exception as error:
         print(f"can not find duplicates: {error}") 
         
finally:  
    """write File"""
    shk.to_csv('sharkoutputwk3.xlsx', index=False)

   
    """print the output"""
    print("output file created succesfully")

