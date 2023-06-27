# CSV to txt-------------------------------------------------------------------

def convert_csv_txt(csv_path,text_path):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        with open(text_path,'w') as text_file:
            for row in csv_reaader:
                text_file.write(','.join(row) + '\n')

