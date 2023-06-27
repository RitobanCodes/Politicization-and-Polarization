import os
import pandas as pd
import time
from docx import Document
import datetime

def extract_body_text(file_path):
    document = Document(file_path)
    body_text = []

    is_body = False
    for paragraph in document.paragraphs:
        if is_body:
            if "Load-Date" in paragraph.text:
                break
            else:
                body_text.append(paragraph.text)
        elif paragraph.text.strip().lower() == "body":
            is_body = True

    return body_text

#==============================================================================

def doc_to_txt(starting_path, destination_path):
    
    weeks = os.listdir(starting_path)
    for week in weeks:
        
        os.makedirs(destination_path+'/'+week)
        articles = os.listdir(starting_path+'/'+week)
        
        for article in articles:
            
            article_path = starting_path+'/'+week+'/'+article
            body = extract_body_text(article_path)
            joined_body = " ".join(body)
            
            article = article.replace(".docx","")
            text = article + "~" + joined_body
            
            #article = article.replace("."," ")
            article = article+".txt"
                    
            text_file = destination_path+'/'+week+'/'+article
            
            with open(text_file, "w", encoding="utf-16") as file:            
                file.write(text)

#==============================================================================
def fix_dates(source):
    dates = os.listdir(source)
    problem = []
    
    for date in dates:
        start_date_str, end_date_str = date.split('-')

        # Extract the date components
        start_day, start_month, start_year = map(int, start_date_str.split('_'))
        end_day, end_month, end_year = map(int, end_date_str.split('_'))

        # Pad the date and month with leading zeros
        start_date = datetime.datetime(start_year + 2000, start_month, start_day).strftime("%d_%m_%Y")
        end_date = datetime.datetime(end_year + 2000, end_month, end_day).strftime("%d_%m_%Y")
        
        folder_name = start_date+'-'+end_date
        os.rename(source+'/'+date,source+'/'+folder_name)
        