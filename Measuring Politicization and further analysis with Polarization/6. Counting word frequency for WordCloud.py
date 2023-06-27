import os
import nltk
import string
import pandas as pd
import time
from collections import Counter


os.chdir("C:/Ritoban/IIMK/Newspaper Articles")

#Combine the text from all files to a single file------------------------------
start_time_combine = time.time()
source = 'Scientist Combined'
def text_combine(source):
    
    outputfile = 'combined.txt'
    combined = ''
    weeks = os.listdir(source)
    with open(outputfile,"a", encoding = 'utf-16') as outfile:
        for week in weeks:
            articles = os.listdir(source + '/' + week)
            for article in articles:
                #Read the .TXT file as a .CSV file
                df = pd.read_csv(source + '/' + week + '/' + article, encoding='utf-16', delimiter='~', header=None)

                try:
                    #Extract the body text from the 2nd column of the dataframe and 
                    #transform it to lowercase
                    body = df.values[0][0] + df.values[0][1].lower()
                    outfile.write(body)
                    outfile.write('\n')
                except AttributeError:
                    outfile.write('\n')
    return combined

combined = text_combine(source)
end_time_combine = time.time()


#Get a list of stopwords
#stopwords = pd.read_csv('Dictionaries/stopwords.csv', header=None)
#stopwords[0] = stopwords[0].apply(lambda x: x.lower())
#stopwords = stopwords.squeeze().to_list()
    
stopwords = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will',
    'with', 'i', 'you', 'your', 'they', 'their', 'them', 'we', 'our', 'us', 'me',
    'my', 'mine', 'myself', 'you', 'your', 'yours', 'yourself', 'he', 'him', 'his',
    'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'we', 'us',
    'our', 'ours', 'ourselves', 'they', 'them', 'their', 'theirs', 'themselves', "'s"
]

punctuations = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}',
    '~', "''", "``"
]


#Reading the .TXT file
file = open("combined.txt", "r", encoding = 'utf-16')
content = file.read().strip()
file.close()

#Remove stopwords and punctuations
content = content.lower()

words = nltk.word_tokenize(content)

start_time_cleaning = time.time()
len1 = len(words)
for word in words:
    words_cleaned = [word for word in words if word not in stopwords and word not in punctuations]
len2 = len(words_cleaned)


#Obtain the frequencies of unique words
word_freq = Counter(words_cleaned)

frequencies = pd.DataFrame(columns = ['Word', 'Frequency'])
for word, freq in word_freq.items():
    frequencies = frequencies.append(pd.Series([word,freq]), ignore_index=True)
    
frequencies['Word'] = frequencies[0]
frequencies['Frequency'] = frequencies[1]
frequencies = frequencies[['Word', 'Frequency']]

frequencies = frequencies.sort_values('Frequency', ascending = False)

frequencies.to_csv("Popular words in Scientist Keyword Articles.csv")
end_time_cleaning = time.time()

print("Time Taken to combine the .TXT files:")
print((end_time_combine-start_time_combine)/60)

print("Time Taken to Create the .CSV file:")
print((end_time_cleaning-start_time_cleaning)/60)
print('Number of stopwords removed:')
print(len1-len2)