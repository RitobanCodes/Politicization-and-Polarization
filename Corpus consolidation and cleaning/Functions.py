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
            file_name = file_name.replace('.docx','.txt')
            outfile = open(out_loc + "/" + file_name, 'w', encoding='utf-8')
            doc = docx2txt.process(infile)

            outfile.write(doc)

        outfile.close()
        infile.close()
        

# Read and Tokenize------------------------------------------------------------
def read_tokenize_csv(text_file, prefix):
    df = pd.DataFrame(columns = ['Name','Topic'])

    f = open(text_file,'r')
    content = f.read()
    
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

#Get the csv lengths-----------------------------------------------------------
def get_csv_length(csv_file_names,location,delim):
    delimiter = delim
    lengths = []
    
    
    for file in csv_file_names:
        file_path = os.path.join(location, file)
        
        nr = 0
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=delimiter)

            # Skip the header row
            #next(reader)

            # Process the remaining rows
            for nrow in reader:
                nr = nr + 1
                
            lengths.append(nr)
            
    return lengths

#Combine the CSVs--------------------------------------------------------------
def combine_csv(csv_file_names,csv_file_lengths,location,delim = "|"):
    perm_df = pd.DataFrame(columns = range(4))
    
    l=0
    for file in csv_file_names:
        
        file_path = os.path.join(location,file)
        
        s = 0
        temp_df = pd.DataFrame(index = range(csv_file_lengths[l]), columns = range(4))
        l += 1
        
        with open(file_path, 'r') as file:
            reader = csv.reader(file,delimiter = delim)
            #Skip the header row
            #next(reader)
        
            #Process the remaining rows
        
            for row in reader:
                for i in range(0,len(row)):
                    temp_df.loc[s][0] = row[0]                   
                    topic = ""
                    for j in range(1,len(row)):
                        topic = topic+row[j]
                    
                    temp_df.loc[s][1] = topic
                s += 1

            perm_df = pd.concat([perm_df,temp_df], axis = 0)
        
    perm_df = perm_df.reset_index()    
    perm_df = perm_df.reindex(range(0,len(perm_df)))
                              
    return perm_df

#Add Dates column--------------------------------------------------------------
def add_dates(dates,lengths,df):
    date = []
    
    for i in range(0,len(lengths)):
        for j in range(0,lengths[i]):
            date.append(dates[i])
                
    df.insert(3,"Date",date)
    
    return df

#Add Filename column--------------------------------------------------------------
def add_filenames(filenames,lengths,df):
    names = []
    name = []
    for i in range(0,len(lengths)):
        name.append(filenames[i].replace('.csv','.txt'))
        for j in range(0,lengths[i]):
            names.append(filenames[i].replace('.csv','.txt'))
                
    df.insert(4,"Filename",names)
    
    return df, name

# CSV to txt-------------------------------------------------------------------
def convert_csv_txt(csv_path,text_path):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        with open(text_path,'w') as text_file:
            for row in csv_reaader:
                text_file.write(','.join(row) + '\n')

