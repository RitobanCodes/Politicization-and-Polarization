import os
import csv
import pandas as pd

os.chdir("C:/Ritoban/IIMK")

Year = 2002
#Get the names of the files and the dates--------------------------------------
folder_location = "Corpus Preprocessing/" + str(Year) + "/3. CSVDocs"

filenames, dates = get_file_names(folder_location)

#Get the lengths of the csv files----------------------------------------------
csv_file_names = filenames
location = folder_location
delim = "|"

csv_lengths = get_csv_length(csv_file_names,location,delim)

#Combine all the csv files-----------------------------------------------------
location = folder_location
delim = "|"

combined = combine_csv(csv_file_names,csv_lengths,location,delim)
combined.columns = ['File index','Name','Topic','','']

#Special Considerations#

specific_name = str(Year)+" Combined.csv"
combined.to_csv("Corpus Preprocessing/" + str(Year) + "/" + specific_name)


