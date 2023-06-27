import os
from pdfminer.high_level import extract_text
import time

def pdf_to_txt(pdf_path, txt_path):
    text = extract_text(pdf_path)

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)



start_time = time.time()

os.chdir("C:/Ritoban/IIMK/Articles")

journal = "Public Administration Review"

path_journal = journal
years = os.listdir(path_journal)

for year in years:
    issues = os.listdir(path_journal+"/"+year)
    for issue in issues:
        pdfs = os.listdir(journal + '/' + year+ "/"+ issue)
        for pdf in pdfs:
            path_pdf = journal + "/" + year + "/" + issue + "/" + pdf
            path_txt = "TEXT/"+journal+"/"+year+"/"+ issue + "/" + pdf.replace("pdf","txt")
            pdf_to_txt(path_pdf,path_txt)
            
end_time = time.time()
(end_time-start_time)/60
    

