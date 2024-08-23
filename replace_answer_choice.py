import pandas as pd
import re

df = pd.read_csv("answer_all_set.csv")
#create new column 1 in df
df['1'] = ''

df1 = pd.read_csv("answer_set1_new.csv")
df2 = pd.read_csv("answer_set2_new.csv")
df3 = pd.read_csv("answer_set3_new.csv")

#merge df1, df2, df3
df4 = pd.concat([df1, df2, df3])

#drop duplicate value
df4 = df4.drop_duplicates()

#sort by length of value in df4 by column 0 descending 
df4['len'] = df4['0'].apply(len)
df4 = df4.sort_values(by='len', ascending=False).drop('len', axis=1)

#remove column unnamed in df4
df4 = df4.loc[:, ~df4.columns.str.contains('^Unnamed')]
print(df4.head(100))
# #save df4 to file csv
# df4.to_csv("answer_set4.csv", index=False)

# fill nan value in df4 by ''    
df4 = df4.fillna('')
Dem = 0
#replace answer in df by value in df4
for i in range(len(df)):
    if df['0'][i] in df4['0'].values:
        print(df['0'][i])
        value = df4['1'][df4['0'] == df['0'][i]].values[0]
        if value is not '':
            Dem += 1
            df['1'][i] = value
            print("    ",df['1'][i])

#save df to file csv
df.to_csv("answer_all_set_new.csv", index=False)
print(df.head())
print(Dem)
print(len(df))