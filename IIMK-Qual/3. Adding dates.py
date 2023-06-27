list_of_dates = []

i = 0
for date in dates:
    for j in range(0,lengths[i]):
        list_of_dates.append(date)
    i = i+1

perm_df.insert(1,'Dates',list_of_dates)

perm_df['Dates'] = perm_df['Dates'].str.replace('-','/')

perm_df.to_csv("Consolidated.csv")
