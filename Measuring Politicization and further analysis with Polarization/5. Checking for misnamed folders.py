list1 = os.listdir("Ritoban/Text-Prompt2")
list2 = os.listdir("Ayushi/Text-4. (Jan 2020 - Apr 2021)")

list2 = list(pd.read_csv('Dictionaries/Covid - Frequency Count2.csv')['Total Week'])

for i in range(0,len(list2)):
    #list2[i] = list2[i].replace("_","-")
    #list2[i] = list2[i][:8]+'_'+list2[i][9:]
    

len(list(set(list2)-set(list1)))

len(list1)
len(list2)
