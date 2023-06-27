def get_csv_length(csv_file_names,location,delim):
    delimiter = delim
    lengths = []
    
    
    for file in csv_file_names:
        file_path = os.path.join(location, file)
        
        nr = 0
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=delimiter)

            # Skip the header row
            next(reader)

            # Process the remaining rows
            for nrow in reader:
                nr = nr + 1
                
            lengths.append(nr)
            
    return lengths

