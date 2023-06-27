import os
import pandas as pd
import time
from docx import Document
import datetime

# Example usage
#file_path = 'Prompt1/01-03-2020_07-03-2020/COVID-19 e`ffect_ govt.cancels womens day fete.docx'
#body = extract_body_text(file_path)

#print("Body text:")
#for line in body:
#    print(line)
    
#==============================================================================
os.chdir('C:/Ritoban/IIMK/Newspaper Articles')

#Input adress of folders containing weekly word docs
starting_folder_path = 'Arjan/Vaccine Scientist'
destination_folder_path ='Arjan/Text-Vaccine Scientist'

doc_to_txt(starting_folder_path,destination_folder_path)


#==============================================================================
full_adress = "C:/Ritoban/IIMK/Newspaper Articles/Arjan/Vaccine Scientist/2"
fix_dates(full_adress)

dates = os.listdir(full_adress)


for date in dates:
    fixed_date = date.replace("_","*").replace("-","_")
    fixed_date = fixed_date.replace("*","-")
    os.rename(source+'/'+date,source+'/'+fixed_date)
