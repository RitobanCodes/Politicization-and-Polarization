import pandas as pd
import os

os.chdir('C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/Covid')

source = 'Monthly Wordfish'
files = os.listdir(source)

Means = pd.DataFrame(columns = ['Article','BJP','Congress','Regional','Others'])
for file in files:
    source_f = source + '/' + file
    
    df = pd.read_csv(source_f)
    df.columns = ['Article','Position','se']
    
    df['Article'] = df['Article'].apply(lambda x: x.replace('.txt',''))
    
    b,c,r,o,lenb,lenc,lenr,leno = 0,0,0,0,0,0,0,0
    for i in range(0,len(df)):
        
        if 'bjp' in df['Article'][i]:
            b  += df['Position'][i]
            lenb += 1
        if 'cong' in df['Article'][i]:
            c += df['Position'][i]
            lenc += 1
        if 'regional' in df['Article'][i]:
            r += df['Position'][i]
            lenr += 1
        if 'bjp' not in df['Article'][i]:
            o += df['Position'][i]
            leno += 1
        
    avg = [b/lenb,c/lenc,r/lenr,o/leno]
        
    row = [file.replace(".csv","").replace("All - ","")] + avg
    row_dict = {'Article':row[0], 'BJP':row[1],'Congress':row[2], 'Regional':row[3],'Others':row[4]}

    Means = Means.append(row_dict, ignore_index = True)

Means.to_csv('Monthly Means - Trimmed2.csv')

