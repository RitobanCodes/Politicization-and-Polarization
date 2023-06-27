import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

os.chdir('C:/Ritoban/IIMK/Newspaper Articles/Wordfish Data/Covid')

mean1 = pd.read_csv('Monthly Means - Trimmed2.csv')
mean1['month'] = mean1['Article'].apply(lambda x: int(''.join(map(str, re.findall(r'\d+', x)))))
mean1 = mean1.sort_values('month')

std1 = pd.read_csv('Monthly StdErr - Trimmed2.csv')
std1 ['month'] = std1 ['Article'].apply(lambda x: int(''.join(map(str, re.findall(r'\d+', x)))))
std1  = std1 .sort_values('month')

mean2 = pd.read_csv('Monthly Means - Not trimmed.csv')
mean2['month'] = mean2['Article'].apply(lambda x: int(''.join(map(str, re.findall(r'\d+', x)))))
mean2 = mean2.sort_values('month')

std2 = pd.read_csv('Monthly StdErr - Not Trimmed.csv')
std2 ['month'] = std2 ['Article'].apply(lambda x: int(''.join(map(str, re.findall(r'\d+', x)))))
std2  = std2 .sort_values('month')

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
x_axis_names = ['Mar-2020','Apr-2020','May-2020','Jun-2020',
                 'Jul-2020','Aug-2020','Sept-2020','Oct-2020',
                 'Nov-2020','Dec-2020','Jan-2021','Feb-2021',
                 'Mar-2021','Apr-2021','May-2021','Jun-2021','Jul-2021',
                 'Aug-2021','Sept-2021','Oct-2021','Nov-2021','Dec-2021',
                 'Jan-2022','Feb-2022','Mar-2022','Apr-2022'
                 ]
#------------------------------------------------------------------------------

#Extract Trimmed Data
x1  = mean1['Article']
y11 = mean1['BJP']
y12 = mean1['Congress']
y13 = mean1['Regional']
y14 = mean1['Others']

y11[np.isnan(y11)] = np.nan
y12[np.isnan(y12)] = np.nan
y13[np.isnan(y13)] = np.nan
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#Extract UnTrimmed Data
#x2 = mean2['Article']
x2 = x1
y21 = mean2['BJP']
y22 = mean2['Congress']
y23 = mean2['Regional']
y24 = mean2['Others']
#------------------------------------------------------------------------------

#Position Across Parties
title = 'Other Parties'
plt.figure(dpi = 300, figsize = (13,8))

#plt.plot(x1, y11,alpha=0.5,linestyle = '--')
#plt.plot(x1, y12,alpha=0.5,linestyle = '--')
plt.plot(x1, y13,alpha=0.5,linestyle = '--')
#plt.plot(x1, y14,alpha=0.5,linestyle = '--')

#plt.scatter(x1, y11,label = 'BJP')
#plt.scatter(x1, y12, label = 'Congress')
plt.scatter(x1, y13, label = 'Other Parties')
#plt.scatter(x1, y14, label = 'Non-BJP Parties')

#plt.scatter(x = x1, y = y12,label = 'Congress')
#plt.scatter(x = x1, y = y13,label = 'Regional')
#plt.scatter(x = x1, y = y14,)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
#Labelling
plt.title(title)
plt.xticks(x1,x_axis_names)
plt.xticks(rotation=45)
plt.xlabel('Time (in months)')
plt.ylabel('Estimated positions across parties')
#plt.legend()
plt.show()

#Difference of Means
title = 'Difference of Means (Trimmed & Not Trimmed) BJP-Congress'
plt.figure(dpi = 300, figsize = (13,8))
#plt.plot(x2, y21,label = 'BJP')
#plt.scatter(x = x2, y = y12,label = 'Congress')
plt.scatter(x = x1, y = y11-y12,label = 'Trimmed')
plt.scatter(x = x2, y = y21-y22,label = 'Not Trimmed')
#plt.scatter(x = x1, y = y14,label = )
plt.title(title)
plt.xticks(x1,x_axis_names)
plt.xticks(rotation=45)
plt.legend()
plt.show()

#BJP and Non-BJP parties (combined)
title = 'BJP and Non-BJP parties'
plt.figure(dpi = 300, figsize = (13,8))
plt.plot(x1, y11,alpha=0.5,linestyle = '--', label = 'BJP')
plt.plot(x1, y14,alpha=0.5,linestyle = '--',label = 'Non-BJP')
plt.scatter(x1, y11)
plt.scatter(x1, y14)
#plt.scatter(x = x1, y = y12,label = 'Congress')
#plt.scatter(x = x1, y = y13,label = 'Regional')
#plt.scatter(x = x1, y = y14,)
plt.title(title)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.xticks(x1,x_axis_names)
plt.xticks(rotation=45)
plt.xlabel('Time (in months)')
plt.ylabel('Estimated positions across parties')
plt.legend()
plt.show()

#---------------------------Difference of means--------------------------------
error1 = std1.apply(lambda x: np.sqrt(x['Congress']**2 + x['BJP']**2), axis=1)
error1 = error1.sort_index()

error2 = std1.apply(lambda x: np.sqrt(x['BJP']**2 + x['Regional']**2), axis=1)
error2 = error2.sort_index()

error3 = std1.apply(lambda x: np.sqrt(x['BJP']**2 + x['Others']**2), axis=1)
error3 = error3.sort_index()

diff1 = (y11-y12).sort_index()
diff2 = (y11-y13).sort_index()
diff3 = (y11-y14).sort_index()

title = 'BJP and Non-BJP Parties'

plt.figure(dpi = 300, figsize = (13,8))

#plt.plot(x1, diff1,alpha=0.3,linestyle = '--',linewidth= 1, color = 'black')
#plt.errorbar(x1,diff1, yerr=error1, fmt='s', color='red',markersize = 1,alpha = 1)
#plt.scatter(x1, diff1,color = 'black',marker = 's',s = 20,alpha = 1,linewidths=2,label = 'Congress & BJP')

#plt.plot(x1, diff2,alpha=0.3,linestyle = '--',linewidth= 1, color = 'black')
#plt.errorbar(x1,diff2, yerr=error2, fmt='s', color='red',markersize = 1,alpha = 1)
#plt.scatter(x1, diff2,color = 'black',marker = 's',s = 20,alpha = 0.6,linewidths=2,label = 'Congress & Other parties')

plt.plot(x1, diff3,alpha=0.3,linestyle = '--',linewidth= 1,color = 'black')
plt.errorbar(x1,diff3, yerr=error3, fmt='s', color='red',markersize = 1)
plt.scatter(x1, diff3,color = 'black',marker = 's',s = 20,alpha = 0.6,linewidths=2,label = 'BJP & Non-BJP Parties')

plt.title(title)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.xticks(x1,x_axis_names)
plt.xticks(rotation=45)
plt.xlabel('Time (in months)')
plt.ylabel('Language Difference across parties')
#plt.legend()
plt.show()