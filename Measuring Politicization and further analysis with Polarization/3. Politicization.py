#import pandas as pd
#import os
#from datetime import datetime
import time

os.chdir("C:/Ritoban/IIMK/Newspaper Articles")

#Import the keywords to be counted in the articles
politician_keywords = pd.read_csv("Dictionaries/Keywords-Politicians.csv",header = None).squeeze().tolist()
scientific_keywords = pd.read_csv("Dictionaries/Keywords-Scientist.csv",header = None).squeeze().tolist()

#------------------------------------------------------------------------------
#no - :
#bjp - :19
#congress - 19:38
#regional - 38:68***
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#1. Choose the keyword list
keyword_list = scientific_keywords
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#2. Input the adress of the folder containing the weekly folders
source = 'Ayushi/Text-Lockdown Science'
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#3. Input the adress of the folder containing the denominator(weekly article counts)
denominator_source = 'Dictionaries/Lockdown - Frequency Count.csv'
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#4. Input the formatting of the date in the folder names
date_format = '%d_%m_%Y'
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#5. Input the index of the last digit of the startinsg week in the folder name
#For example if the folder name is "02-02-2020_02-08-2020" then a = 9
a = 9
#Input the index of the first digit of the ending week in the folder name
#For example if the folder name is "02-02-2020_02-08-2020" then b = 11
b = 11
#------------------------------------------------------------------------------

start_time = time.time()
df, raw_df, problem, denom = count_wordoccurence(source,denominator_source,date_format,stweek_index = a+1,enweek_index = b)
end_time = time.time()

# "raw_df" contains the names of the files
# "problem" contains the location of those 
#folders that are empty for some reason
print("Time taken to run:")
print(end_time-start_time)

#!!!!!!!!!!!!!Possible error:
#   Weekly names of the folders are not in standard format

#Join two dataframes
#df = pd.concat([df2,df1], axis = 0).sort_index()
#df[['Frequencies', 'Articles', 'Average']].to_csv('Dictionaries/2. Covid - Scientific Average.csv')

df[['Frequencies','Articles','Average']].to_csv('Dictionaries/7. Lockdown - Scientific Average.csv')
