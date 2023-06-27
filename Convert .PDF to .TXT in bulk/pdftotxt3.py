import fitz
import os
import time

def pdf_to_txt(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()

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