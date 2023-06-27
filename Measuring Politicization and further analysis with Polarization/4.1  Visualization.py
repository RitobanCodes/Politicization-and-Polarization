import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
import os
from wordcloud import WordCloud
import time

os.chdir("C:/Ritoban/IIMK/Newspaper Articles")


#Function to calculate Moving Averages--------------------------------
def calc_MA(y):
    MA = []
    for i in range(0,len(y)-3):
        s = 0
        for j in range(0,4):
            s += y[i+j]
        s /= 4
        MA.append(s)
        
    return MA
#---------------------------------------------------------------------

#==========================================================================================================================================
#-----------------COVID-19 Actor Dictionaries (Politicians and Scientists)-------------------------------------------------------------------
#==========================================================================================================================================

x1 = pd.read_csv('Dictionaries/1. Covid - Political Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/1. Covid - Political Average.csv')['Average']
label1 = 'Politicians'

x2 = pd.read_csv('Dictionaries/2. Covid - Scientific Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/2. Covid - Scientific Average.csv')['Average']
label2 = 'Scientists'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)  
    
ma_dates1 = pd.date_range(start='2020-02-02',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-02-02',freq = 'W' ,periods = len(MA2))

title = 'COVID-19 Actor Dictionaries (Politicians and Scientists)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

#plt.scatter(x3,y3,color = 'green',marker = 'd', s = 20,alpha = 0.7)
#plt.plot(ma_dates_offset3,MA3,color = 'Green',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
plt.text(x=0.1,
         y=0.6,
         s="Scientists",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'grey',
         weight = 'bold'
         )
plt.text(x=0.15,
         y=0.15,
         s="Politicians",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'black',
         weight = 'bold'
         )

#Show Legend
plt.legend()

#Show Plot
plt.show()    


#==========================================================================================================================================
#-----------------COVID Vaccine Actor Dictionaries (Politician and Scientist)-------------------------------------------------------------------
#==========================================================================================================================================

x1 = pd.read_csv('Dictionaries/11. Vaccine - Political Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/11. Vaccine - Political Average.csv')['Average']
label1 = 'Politicians'

x2 = pd.read_csv('Dictionaries/12. Vaccine - Scientific Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/12. Vaccine - Scientific Average.csv')['Average']
label2 = 'Scientists'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)  
    
ma_dates1 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA2))

title = 'COVID Vaccine Actor Dictionaries (Politicians and Scientists)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

#plt.scatter(x3,y3,color = 'green',marker = 'd', s = 20,alpha = 0.7)
#plt.plot(ma_dates_offset3,MA3,color = 'Green',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
plt.text(x=0.3,
         y=0.7,
         s="Scientists",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'grey',
         weight = 'bold'
         )
plt.text(x=0.05,
         y=0.3,
         s="Politicians",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'black',
         weight = 'bold'
         )

#Show Legend
plt.legend()

#Show Plot
plt.show()    

#==========================================================================================================================================
#-----------------COVID Lockdown Actor Dictionaries (Politician and Scientist)-------------------------------------------------------------------
#==========================================================================================================================================

x1 = pd.read_csv('Dictionaries/6. Lockdown - Political Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/6. Lockdown - Political Average.csv')['Average']
label1 = 'Politicians'

x2 = pd.read_csv('Dictionaries/7. Lockdown - Scientific Average.csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/7. Lockdown - Scientific Average.csv')['Average']
label2 = 'Scientists'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)  
    
ma_dates1 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA2))

title = 'COVID Vaccine Actor Dictionaries (Politicians and Scientists)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

#plt.scatter(x3,y3,color = 'green',marker = 'd', s = 20,alpha = 0.7)
#plt.plot(ma_dates_offset3,MA3,color = 'Green',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
plt.text(x=0.15,
         y=0.05,
         s="Scientists",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'grey',
         weight = 'bold'
         )
plt.text(x=0.05,
         y=0.25,
         s="Politicians",
         transform=plt.gca().transAxes,
         fontsize = 12,
         color = 'black',
         weight = 'bold'
         )

#Show Legend
plt.legend()

#Show Plot
plt.show()  

