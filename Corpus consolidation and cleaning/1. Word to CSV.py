import os
import pandas as pd
import docx2txt
import nltk
from fuzzywuzzy import fuzz
import time

os.chdir("C:/Ritoban/IIMK")

Year = str(1988)

folder_location = "Corpus Preprocessing/"+Year+"/1. WordDocs"
#Get file names and dates------------------------------------------------------
filenames, dates = get_file_names(folder_location)


#Convert from .DOC to .TXT-----------------------------------------------------

out_location = "Corpus Preprocessing/"+Year+"/2. UncleanedTextDocs"
doc_to_txt(folder_location,out_location)


#Read .TXT, tokenize and convert to CSV----------------------------------------
txt_location = "Corpus Preprocessing/"+Year+"/2. UncleanedTextDocs"
prefix = ['DR.', 'MR.', 'SHRI', 'SHRIMATI', 'PROF', 'KUMARI','COL.','BEGAM']

start_time = time.time()
combined = read_tokenize_csv(txt_location, prefix)
end_time = time.time()
(end_time-start_time)/60

combined.to_csv("Corpus Preprocessing/"+Year+"/"+Year+" Combined.csv")

fuzz.ratio("SHRJ","SHRI")
