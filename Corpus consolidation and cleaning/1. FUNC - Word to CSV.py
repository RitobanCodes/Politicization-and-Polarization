#Get the file names------------------------------------------------------------
def get_file_names(folder_location):
    dates = []

    file_names = os.listdir(folder_location)

    for file in file_names:
        dates.append(file[10:20])
        
    return file_names, dates


#.DOC to .TXT------------------------------------------------------------------
def doc_to_txt(word_location, out_loc):
    word_file_names = os.listdir(word_location)

    for file_name in word_file_names:
        
        loc = word_location+"/"+file_name
        with open(loc, 'rb') as infile:
            outfile = open(out_loc + "/" + file_name+'.txt', 'w', encoding='utf-8')
            doc = docx2txt.process(infile)

            outfile.write(doc)

        outfile.close()
        infile.close()
        

# Read and Tokenize------------------------------------------------------------
def read_tokenize_csv(text_files_folder, prefix):
    text_file_names = os.listdir(text_files_folder)
    df = pd.DataFrame(columns = ['Name','Topic'])

    for text_file in text_file_names:
        f = open(text_files_folder+"/"+text_file,'r')
        content = f.read()
        del f
        
        tokens = nltk.word_tokenize(content)
        
        #fixing prefixes
        for i in range(0,len(tokens)):
            ratios = []
            for pref in prefix:
                ratios.append(fuzz.ratio(pref,tokens[i]))
                
            ratio = max(ratios)
            ratio_ind = ratios.index(ratio)
            
            if ratio > 72:
                tokens[i] = prefix[ratio_ind]
        
        #Creating the csv file
        for i in range(len(tokens)):
            name = ""
            topic = ""
            j= 0
            if tokens[i] in prefix:
                j = i+1
                while(tokens[j].isupper()):
                    name = name+" " +tokens[j]
                    j = j+1
                    
                while(tokens[j] not in prefix and j<len(tokens)-1):
                    topic = topic +" " + tokens[j]
                    j = j+1
            
            if name != '':
                a = topic.find(":")
                b = topic.find(";")
                c = [min(a,b) if a>-1 and b>-1 else max(a,b)]
                
                if  c[0]<=40 and c[0]>=0:
                    name = name + topic[:c[0]]
                    topic = topic[c[0]+1:]
                
                new_row = pd.DataFrame([{'Name':name,'Topic':topic}])
                df= pd.concat([df,new_row],ignore_index = True)

    
    return df

#Adding Dates------------------------------------------------------------------


