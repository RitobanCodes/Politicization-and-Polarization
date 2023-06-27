def combine_csv(csv_file_names,csv_file_lengths,location,delim = "|"):
    perm_df = pd.DataFrame(columns = range(5))
    
    l=0
    for file in csv_file_names:
        
        file_path = os.path.join(location,file)
        
        s = 0
        temp_df = pd.DataFrame(index = range(csv_file_lengths[l]), columns = ['Name','Topic1','Topic2','Dates'])
        l += 1
        
        with open(file_path, 'r') as file:
            reader = csv.reader(file,delimiter = delim)
            #Skip the header row
            next(reader)
        
            #Process the remaining rows
        
            for row in reader:
                for i in range(0,len(row)):
                    temp_df.loc[s][0] = row[0]                   
                    topic = ""
                    for j in range(2,len(row)):
                        topic = topic+row[j]
                    
                    temp_df.loc[s][1] = topic
                s += 1

            perm_df = pd.concat([perm_df,temp_df], axis = 0)
        
    return perm_df

l= 0
perm_df = pd.DataFrame(columns = range(5))
for file in csv_file_names:
    
    file_path = os.path.join(location,file)
    
    s = 0
    temp_df = pd.DataFrame(index = range(csv_lengths[l]), columns = range(10))
    l = l+1
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=delim)

        # Skip the header row
        next(reader)

        # Process the remaining rows
        
        for row in reader:
            for i in range(0,len(row)):
                temp_df.loc[s][i] = row[i]
            s = s+1
            
    perm_df = pd.concat([perm_df,temp_df], axis = 0)