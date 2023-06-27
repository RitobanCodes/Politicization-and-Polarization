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
#-----------------COVID-19 Politician Dictionaries (BJP, Congress and Others)--------------------------------------------------------------
#==========================================================================================================================================

x1 = pd.read_csv('Dictionaries/3. Covid - Political Average (BJP).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/3. Covid - Political Average (BJP).csv')['Average']
label1 = 'BJP'

x2 = pd.read_csv('Dictionaries/4. Covid - Political Average (Congress).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/4. Covid - Political Average (Congress).csv')['Average']
label2 = 'Congress'

x3 = pd.read_csv('Dictionaries/5. Covid - Political Average (Regional).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y3 = pd.read_csv('Dictionaries/5. Covid - Political Average (Regional).csv')['Average']
label3 = 'Others'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)
MA3 = calc_MA(y3)
    
ma_dates1 = pd.date_range(start='2020-02-02',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-02-02',freq = 'W' ,periods = len(MA2))
ma_dates3 = pd.date_range(start='2020-02-02',freq = 'W' ,periods = len(MA3))

title = 'COVID-19 Politicians Dictionaries (BJP, Congress and Others)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

plt.scatter(x3,y3,facecolors = 'white',edgecolors = 'darkgrey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates3,MA3,color = 'darkgrey',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
#plt.text(x=0.1,
#         y=0.6,
#         s="Scientist",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'grey',
#         weight = 'bold'
#         )
#plt.text(x=0.15,
#         y=0.15,
#         s="Politician",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'black',
#         weight = 'bold'
#         )

#Show Legend
plt.legend()

#Show Plot
plt.show()

#=====================================================================================================================================================
#----------------------------COVID-19 Vaccine Dictionaries (BJP, Congress and Others)--------------------------------------------------------------
#=====================================================================================================================================================

x1 = pd.read_csv('Dictionaries/13. Vaccine - Political Average (BJP).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/13. Vaccine - Political Average (BJP).csv')['Average']
label1 = 'BJP'

x2 = pd.read_csv('Dictionaries/14. Vaccine - Political Average (Congress).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/14. Vaccine - Political Average (Congress).csv')['Average']
label2 = 'Congress'
    
x3 = pd.read_csv('Dictionaries/15. Vaccine - Political Average (Regional).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y3 = pd.read_csv('Dictionaries/15. Vaccine - Political Average (Regional).csv')['Average']
label3 = 'Others'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)
MA3 = calc_MA(y3)
    
ma_dates1 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA2))
ma_dates3 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA3))

title = 'COVID-19 Vaccine Politicians Dictionaries (BJP, Congress and Others)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

plt.scatter(x3,y3,facecolors = 'white',edgecolors = 'darkgrey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates3,MA3,color = 'darkgrey',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
#plt.text(x=0.1,
#         y=0.6,
#         s="Scientist",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'grey',
#         weight = 'bold'
#         )
#plt.text(x=0.15,
#         y=0.15,
#         s="Politician",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'black',
#         weight = 'bold'
#         )

#Show Legend
plt.legend()

#Show Plot
plt.show()

#=====================================================================================================================================================
#----------------------------COVID-19 Lockdown Dictionaries (BJP, Congress and Others)--------------------------------------------------------------
#=====================================================================================================================================================

x1 = pd.read_csv('Dictionaries/8. Lockdown - Political Average (BJP).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y1 = pd.read_csv('Dictionaries/8. Lockdown - Political Average (BJP).csv')['Average']
label1 = 'BJP'

x2 = pd.read_csv('Dictionaries/9. Lockdown - Political Average (Congress).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y2 = pd.read_csv('Dictionaries/9. Lockdown - Political Average (Congress).csv')['Average']
label2 = 'Congress'  
    
x3 = pd.read_csv('Dictionaries/10. Lockdown - Political Average (Regional).csv')['Starting Week'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
y3 = pd.read_csv('Dictionaries/10. Lockdown - Political Average (Regional).csv')['Average']
label3 = 'Others'

#Calculating Moving Averages
MA1 = calc_MA(y1)
MA2 = calc_MA(y2)
MA3 = calc_MA(y3)
    
ma_dates1 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA1))
ma_dates2 = pd.date_range(start='2020-03-15',freq = 'W' ,periods = len(MA2))
ma_dates3 = pd.date_range(start='2020-03-12',freq = 'W' ,periods = len(MA3))

title = 'COVID-19 Lockdown Politicians Dictionaries (BJP, Congress and Others)'

plt.figure(dpi = 300, figsize = (13,8))

plt.scatter(x1,y1,facecolors = 'white', edgecolors = 'black',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates1,MA1,color = 'black',linestyle = '-',label = label1)

plt.scatter(x2,y2,facecolors = 'white',edgecolors = 'grey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates2,MA2,color = 'grey',linestyle = '-',label = label2)

plt.scatter(x3,y3,facecolors = 'white',edgecolors = 'darkgrey',marker = 'o', s = 20,alpha = 0.7)
plt.plot(ma_dates3,MA3,color = 'darkgrey',linestyle = '-',label = label3)

#Remove Spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Add Labels
plt.ylabel('Mean mentions per newspaper article')
plt.xlabel('Week')
plt.title(title,loc = 'left', fontdict={'fontsize': 16, 'fontweight': 'bold'})

#Add Texts
#plt.text(x=0.1,
#         y=0.6,
#         s="Scientist",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'grey',
#         weight = 'bold'
#         )
#plt.text(x=0.15,
#         y=0.15,
#         s="Politician",
#         transform=plt.gca().transAxes,
#         fontsize = 12,
#         color = 'black',
#         weight = 'bold'
#         )

#Show Legend
plt.legend()

#Show Plot
plt.show() 



