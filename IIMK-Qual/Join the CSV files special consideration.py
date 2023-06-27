#removing dates from topic columns
for row in range(1,271):
    split_texts = combined.at[row,'Topic'].split()[1:]
    combined.at[row,'Topic'] = " ".join(split_texts)
del split_texts
