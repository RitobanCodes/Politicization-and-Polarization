import os
import csv
import pandas as pd
import docx2txt
import nltk
from fuzzywuzzy import fuzz
import time

os.chdir("C:/Ritoban/IIMK")

Year = str(1988)

#===============================WORD TO TXT====================================

folder_location = "Data/"+Year+"/1. WordDocs"

#Get file names and dates
word_filenames, dates = get_file_names(folder_location)

#Convert from .DOC to .TXT
out_location = "Data/"+Year+"/2. UncleanedTextDocs"
doc_to_txt(folder_location,out_location)

#Read .TXT, tokenize and convert to CSV
txt_location = "Data/"+Year+"/2. UncleanedTextDocs"
prefix = ['DR.', 'MR.', 'SHRI', 'SHRIMATI', 'PROF', 'KUMARI','COL.','BEGAM']

start_time = time.time()
combined = read_tokenize_csv(txt_location, prefix)
end_time = time.time()
(end_time-start_time)/60

combined.to_csv("Corpus Preprocessing/"+Year+"/"+Year+" Combined.csv")


#===============================TXT to CSV=====================================
csv_location = "Data/"+Year+"/3. CSVDocs/"
txt_location = "Data/"+Year+"/2. UncleanedTextDocs"
txt_files = os.listdir(txt_location)

prefix = ['DR.', 'MR.', 'SHRI', 'SHRIMATI', 'PROF', 'KUMARI','COL.','BEGAM']


for file in txt_files:
    df = read_tokenize_csv(txt_location+'/'+file,prefix)
    df.to_csv(csv_location+file.replace('.txt','.csv'))


#===============================JOIN THE CSVs==================================

#Get the names of the files and the dates
folder_location = "Data/" + Year + "/3. CSVDocs"

filenames, dates = get_file_names(folder_location)

#Get the lengths of the csv files
csv_file_names = filenames
location = folder_location
delim = "|"

csv_lengths = get_csv_length(csv_file_names,location,delim)


#Combine all the csv files
start = time.time()

location = folder_location
delim = "|"

combined = combine_csv(csv_file_names,csv_lengths,location,delim)
combined.columns = ['File index','Name','Topic','','']

end = time.time()
(end-start)/60

#Special Considerations#

#Add dates
combined = add_dates(dates, csv_lengths, combined)

specific_name = Year+" Combined.csv"
combined.to_csv("Data/" + Year + "/" + specific_name)
combined.to_csv("Data/" + Year + "/" + specific_name.replace(".csv",".txt"))

#==========================EXTRACTING CLEANED TXT==============================

combined, txt_file_names = add_filenames(csv_file_names,csv_lengths,combined)
#combined = combined.drop(combined.index[0])

date_wise = combined.groupby('Filename')

delim = ','
txtloc = 'Data/'+Year+'/4. CleanedTextDocs/'

start = time.time()
for txtname in txt_file_names:
    date_df = date_wise.get_group(txtname)
    date_df.to_csv(txtloc+txtname,sep =delim, index = True)
end = time.time()
(end-start)
