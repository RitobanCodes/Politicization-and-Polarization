import pandas as pd
import os
from datetime import datetime

#A function to return the frequency of a set of words or sequences of words
#from a long string
def politicization_freq(source,keywords):
    
    #Read the .TXT file as a .CSV file
    df = pd.read_csv(source, encoding='utf-16', delimiter='~', header=None)
    
    try:
        #Extract the body text from the 2nd column of the dataframe and 
        #transform it to lowercase
        body =df.values[0][0].lower() +  df.values[0][1].lower()
    except AttributeError:
        return 0
    
    #Transform the keywords to lowercase
    keywords = [element.lower() for element in keywords]
    
    #Calculated the frequency of the keywords in the body text
    freq = 0
    for keyword in keywords:
        a = body.count(keyword)
        freq += a
    return freq

#==============================================================================

def count_wordoccurence(source, denominator_source,date_format = '%d-%m-%Y', stweek_index=10,enweek_index=11):
    
    #Get a list of all the weekly folder names
    weeks = os.listdir(source)
    
    week_name, title,frequencies,nfiles = [],[],[],[]
    problem = []
    
    for week in weeks:
        #Get a list of all the articles under 'week'
        files = os.listdir(source + '/' + week )
        
        #Get the number of articles for 'week', discard empty weeks
        nfiles.append(len(files))
        nfiles = [x for x in nfiles if x != 0]
        
        if len(files)>0:
            for file in files:
                source_path = source + '/' + week + '/' + file
                
                #Calculate the frequency of the keywords in the 'file' article
                #Save the frequency, week of the article and title of the article
                frequencies.append(politicization_freq(source_path,keyword_list))
                week_name.append(week)
                title.append(file)
        else:
            #If the week is empty, then return the location of the week folder
            #as a problem
            source_path = source + '/' + week + '/' + file
            problem.append(source_path)
     
    frequency_df = pd.DataFrame({'Week':week_name, 'Title':title, 'Frequencies' : frequencies})
    
    #Extracting the starting and ending weeks from the folder names
    frequency_df['Starting Week'] = frequency_df['Week'].apply(lambda x: x[0:stweek_index] )  
    frequency_df['Ending Week'] = frequency_df['Week'].apply(lambda x: x[enweek_index:])      

    #Converting string date objects to datetime objects
    frequency_df['Starting Week'] = frequency_df['Starting Week'].apply(lambda x: datetime.strptime(x,date_format).date() )   

    temp_df = frequency_df[['Starting Week', 'Frequencies']]

    #Calculating the sum of per article frequencies weekly
    final_df = temp_df.groupby('Starting Week')['Frequencies'].sum() 
    
    final_df = final_df.to_frame()
    final_df['No. of Articles'] = nfiles
    
    #Reading the .CSV with the count of articles per week
    count = pd.read_csv(denominator_source)
    count['Starting Week'] = count['Total Week'].apply(lambda x: x[:10])

    denominator = count[['Starting Week', 'Articles']]
    denominator.index = denominator['Starting Week'].apply(lambda x: datetime.strptime(x,"%d-%m-%Y").date())

    
    #Calculating the average
    #final_df['Average'] = final_df['Frequencies']/final_df['No. of Articles']
    #final_df = final_df.sort_index()
    
    final_df = final_df.merge(denominator, left_index = True, right_index=True, how = 'inner')
    final_df['Average'] = final_df['Frequencies']/final_df['Articles']
    final_df = final_df.sort_index()
    
    return final_df, frequency_df, problem, denominator
        
  
    