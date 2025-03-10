# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:09:18 2024

@author: esina
"""

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
        "remove all duplicate rows"
        shk_unique = shk.drop_duplicates()
        print("\nshk afer removing duplicates:")
        print(shk_unique)
    except Exception as error:
         print(f"can not find duplicates: {error}") 
        
    try:
        """Replace missing values in the country column with USA if it says Florida in the Area column"""
        shk.loc[(shk['Area'] == 'Florida') & (shk['Country'].isnull()), 'Country'] = 'USA'
    except Exception as error:
         print(f"can not replace missing values: {error}")
         
    try:
        """write File"""
        shk.to_csv('sharkoutputwk4(3).csv', index=False)
    except Exception as error:
         print(f"can not write file: {error}")
         
    try:
        """Ensure the data frame is a data frame"""
        print(type(shk))
    except Exception as error:
             print(f"not a dataframe: {error}")
    try:
        """find out the structure of the data frame"""
        print(shk.head())
        print(shk.columns)
    except Exception as error:
         print(f"structure unclear: {error}")
 
finally:
        """Filter out rows with no values and ones that say no shark involvement"""
        if 'Country' in shk.columns and'Species ' in shk.columns:
            filtered_shk = shk.dropna(subset=['Country', 'Species '])
            filtered_shk = filtered_shk[~filtered_shk['Species '].str.contains('No shark involvement', case=False, na=False)]
            
            """Group by country and count the the number of attacks"""
            shark_attack_counts =filtered_shk['Country'].value_counts()
            
            """Display all rows"""
            pd.set_option('display.max_rows', len(shark_attack_counts))
            """Display results"""
            print("Number of shark attacks by country:")
            print(shark_attack_counts)
            pd.reset_option('display.max_rows')
        else:
            print("The required 'columns' and/or 'Species ' do not exist")
            
#print first five and last five rows to look at data
print(shk.head())
print(shk.tail())