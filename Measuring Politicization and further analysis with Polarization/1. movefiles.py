import os
import shutil
import zipfile
import pandas as pd

os.chdir('C:/Ritoban/IIMK/Newspaper Articles')

filenames1 = pd.read_csv('Prompt1.csv',header = None).squeeze().tolist()
filenames2 = pd.read_csv('Prompt2.csv', header = None).squeeze().tolist()
filenames3 = pd.read_csv('Prompt3.csv', header = None).squeeze().tolist()

rawnames1 = os.listdir('C:/Ritoban/IIMK/Newspaper Articles/1')
rawnames2 = os.listdir('C:/Ritoban/IIMK/Newspaper Articles/2')
rawnames3 = os.listdir('C:/Ritoban/IIMK/Newspaper Articles/3')

for foldername in filenames3:
    
    os.makedirs('Prompt3/'+foldername)
    
    temp = []
    for name in rawnames3:
        if foldername in name:
            temp.append(name)
    
        
    for name in temp:
        zip_path = '3/'+name
        destination_folder = 'Prompt3/'+foldername
        
        # Extract the zipped folder
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall('temp_extracted_folder')
        
        # Iterate through the extracted files
        for root, dirs, files in os.walk('temp_extracted_folder'):
            for file in files:
                # Check if the file is a Word document
                if file.endswith('.docx') or file.endswith('.doc'):
                    # Create the destination path for the Word document
                    destination_path = destination_folder+'/'+file
                    # Move the Word document to the destination folder
                    shutil.move(os.path.join(root, file), destination_path)
                    
        # Remove the temporary extracted folder
        shutil.rmtree('temp_extracted_folder')





