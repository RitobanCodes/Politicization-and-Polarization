import PyPDF2
import os
import time


def pdf_to_txt(pdf_path, output_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

start_time = time.time()

os.chdir("C:/Ritoban/IIMK/Articles")

journal = "Public Administration Quaterly"

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