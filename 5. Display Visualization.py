# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:12:44 2024

@author: esina
"""

"""import pandas"""
import pandas as pd

"""Import Matplotlib"""
import matplotlib.pyplot as plt

"""read file in with the new encoding"""
shrk = pd.read_csv(r'C:\Users\esina\OneDrive\Desktop\Rasmussen\Data Quality in Analytics\OriginalSharkAttack.csv', dtype = 'str', encoding = 'Windows-1252', delimiter = ',')
try:
    try:
        "remove all duplicate rows"
        shrk_unique = shrk.drop_duplicates()
        print("\nshk afer removing duplicates:")
        print(shrk_unique)
    except Exception as error:
         print(f"can not find duplicates: {error}") 

    try:
        """Filter out rows with no values and ones that say no shark involvement"""
        if 'Country' in shrk.columns and'Species ' in shrk.columns:
            filtered_shrk = shrk.dropna(subset=['Country', 'Species '])
            filtered_shrk = filtered_shrk[~filtered_shrk['Species '].str.contains('No shark involvement', case=False, na=False)]
    except Exception as error:
         print(f"can not filter: {error}")

    try:
        """replace empty spaces with not_available"""
        shrk['Species '] = shrk['Species '].fillna('Not-Available')
    except Exception as error:
             print(f"can not replace empty spaces : {error}")
    try:
        """Replace missing values in the country column with USA if it says Florida in the Area column"""
        shrk.loc[(shrk['Area'] == 'Florida') & (shrk['Country'].isnull()), 'Country'] = 'USA'
    except Exception as error:
             print(f"can not replace missing values : {error}")
             
    try:
        """filter out countries with less than a certain number of shark attacks """
        shrk = shrk.groupby('Country').filter(lambda x: len(x) > 100)
    except Exception as error:
                 print(f"can not filter out countries : {error}")

finally:
    """Show all columns to check changes went into effect"""
    pd.set_option('display.max_columns', None)
    """Display the first few rows of data"""
    print(shrk.head())


"""Pie Chart"""
shrk.groupby('Country').size().plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Shark Attacks per Country')
plt.show()

"""Line graph"""
shrk.groupby('Country').size().plot(kind='line')
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('Number of Shark Attacks')
plt.title ('Shark Attacks per Country')
plt.show()

"""Bar Chart"""
shrk.groupby('Country').size().plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Number of Shark Attacks')
plt.title ('Shark Attacks per Country')
plt.show()