#Get the file names------------------------------------------------------------
def get_file_names(folder_location):
    dates = []

    file_names = os.listdir(folder_location)

    for file in file_names:
        dates.append(file[10:20])
        
    return file_names, dates


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
