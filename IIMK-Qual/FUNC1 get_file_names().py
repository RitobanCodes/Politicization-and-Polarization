def get_file_names(folder_location):
    dates = []

    file_names = os.listdir(folder_location)

    for file in file_names:
        dates.append(file[10:20])
        
    return file_names, dates