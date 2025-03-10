# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:55:28 2024

@author: esina
"""

#import pandas
import pandas as pd

#Import Matplotlib
import matplotlib.pyplot as plt

#read file in with encoding
try:
    shrk = pd.read_csv(r'C:\Users\esina\OneDrive\Desktop\Rasmussen\Data Quality in Analytics\OriginalSharkAttack.csv', 
                       dtype = 'str', encoding = 'Windows-1252', delimiter = ',')
except Exception as error:
         print(f"can not import file: {error}") 
         
#######################################################
"""Analyze the dataset"""
"""Display all column"""
pd.set_option('display.max_columns', None)

""""print first five and last five rows to look at data"""
print(shrk.head())
print(shrk.tail())

"""Check for missing data"""
"""count of missing values in each column"""
missing_data =shrk.isnull().sum()
print(missing_data)

"""Examine data types of each column"""
print(shrk.dtypes)

"""count duplicate rows"""
duplicate_rows = shrk.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

###########################################################
#resolve data issues

"remove all duplicate rows"
shrk_unique = shrk.drop_duplicates()
print("\nshark afer removing duplicates:")
print(shrk_unique)


"""Filter out rows with no values and ones that say no shark involvement"""
if 'Country' in shrk.columns and'Species' in shrk.columns:
    filtered_shrk = shrk.dropna(subset=['Country', 'Species'])
    filtered_shrk = filtered_shrk[~filtered_shrk['Species'].str.contains('No shark involvement', case=False, na=False)]


"""replace empty spaces with not_available"""
shrk['Species'] = shrk['Species'].fillna('Not-Available')


"""Replace missing values in the country column with USA if it says Florida in the Area column"""
shrk.loc[(shrk['Area'] == 'Florida') & (shrk['Country'].isnull()), 'Country'] = 'USA'

     
"""filter out countries with less than a certain number of shark attacks """
shrk = shrk.groupby('Country').filter(lambda x: len(x) > 17)
    

"""Show all columns to check changes went into effect"""
pd.set_option('display.max_columns', None)
"""Display the first few rows of data"""
print(shrk.head())
print(shrk.tail())
###############################################################
#write out file
try:
    """write File"""
    shrk.to_csv('sharkoutputweek6.csv', index=False)
except Exception as error:
     print(f"can not write file: {error}")
###############################################################
#count shark attacks by country

"""Filter out rows with no values and ones that say no shark involvement"""
if 'Country' in shrk.columns and'Species' in shrk.columns:
     filtered_shrk = shrk.dropna(subset=['Country', 'Species'])
     filtered_shrk = filtered_shrk[~filtered_shrk['Species'].str.contains('No shark involvement', case=False, na=False)]
     
     """Group by country and count the the number of attacks"""
     shark_attack_counts =filtered_shrk['Country'].value_counts()
     
     """Display all rows"""
     pd.set_option('display.max_rows', len(shark_attack_counts))
     """Display results"""
     print("Number of shark attacks by country:")
     print(shark_attack_counts)
     pd.reset_option('display.max_rows')
else:
     print("The required 'columns' and/or 'Species' do not exist")

################################################################
# Line, Pie and Bar charts

"""Pie Chart"""
shrk.groupby('Country').size().plot(kind='pie', autopct = None, labels = None)
plt.axis('equal')
plt.title('Shark Attacks per Country')
plt.show()

"""Line graph"""
shrk.groupby('Country').size().plot(kind='line')
plt.xticks(rotation=10, fontsize = 6)
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