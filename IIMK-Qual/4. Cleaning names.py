import pandas as pd
import numpy as np
import os

from fuzzywuzzy import fuzz, process

os.chdir("C:/Ritoban/IIMK/Data/")

consolidated = pd.read_csv("1. Consolidated.csv")
key = pd.read_csv('key.csv')

corr_names = key['NAMES']
rec_names = consolidated['0']

# getting rid of nan values in rec names
nan_indices = [index for index in range(len(rec_names)) if isinstance(rec_names[index], float) and np.isnan(rec_names[index])]

for x in nan_indices:
    rec_names[x] = 'x'

corrected_names = []
problems = []

for name in rec_names:
    
    ratio = []
    
    for i in range(0,len(corr_names)):
        ratio.append(fuzz.ratio(name,corr_names[i]))
        
    max_ratio = max(ratio)
    max_index = ratio.index(max_ratio)
    
    if max_ratio >=  40:
        corrected_names.append(corr_names[max_index])
    else:
        corrected_names.append("None")
        problems.append(name)
        
corrected_names_df = pd.DataFrame(index = range(27030),columns = range(2))
corrected_names_df[0] = rec_names
corrected_names_df[1] = corrected_names

corrected_names_df.to_csv('Corrected names.csv')

# rechecking

corrected = pd.read_csv("2. Corrected names.csv", na_values=[''])
corrected = corrected['Corrected']
corrected = corrected.fillna('NotApplicable')
key = pd.read_csv('key.csv')
key = key['NAMES']

# getting rid of nan values in rec names
ser = corrected
nan_indices = [index for index in range(len(ser)) if isinstance(ser[index], float) and np.isnan(ser[index])]

for x in nan_indices:
    rec_names[x] = 'x'
    
    
rechecked = []
problems = []

for name in corrected:
    
    ratio = []
    
    for i in range(0,len(key)):
        ratio.append(fuzz.ratio(name,key[i]))
        
    max_ratio = max(ratio)
    max_index = ratio.index(max_ratio)
    
    if max_ratio >=  75:
        rechecked.append(key[max_index])
    else:
        rechecked.append(name)
        problems.append(name)

rechecked_df = pd.DataFrame(index = range(27030), columns = ['Actual','Corrected','Rechecked'])
actual = pd.read_csv('2. Corrected names.csv')['Actual']

rechecked_df['Actual'] = actual
rechecked_df['Corrected'] = corrected
rechecked_df['Rechecked'] = rechecked

rechecked_df.to_csv('3. Rechecked names.csv')
