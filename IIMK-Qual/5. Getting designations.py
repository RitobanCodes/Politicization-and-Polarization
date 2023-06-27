import pandas as pd
import numpy as np
import os


os.chdir("C:/Ritoban/IIMK/Data/")
df = pd.read_csv('3. Rechecked names.csv')
rech_name = df['Rechecked']
rech_name = rech_name.fillna('NotApplicasble')
    
des = []

for i in range(0,len(df)):
    name = df['Actual'][i]
    if ("SPEAKER" in rech_name[i]) or ("CHAIR" in rech_name[i]):
        des.append("CHAIR")
    elif 'MINISTER' in name:
        des.append('MP')
    else:
        des.append("GVMT")
        
df.insert(2,"Designation",des)

df.to_csv('4. Rechecked names with designation.csv')
