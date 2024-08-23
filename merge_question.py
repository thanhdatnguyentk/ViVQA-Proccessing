import pandas as pd
import numpy as np
import re
#turn off warning
pd.SettingWithCopyWarning = False
df1 = pd.read_csv("random_sample.csv")
df2 = pd.read_csv("filtered_questions.csv")


pattern = "(?<=answer':\s')(?:[^']+|\s+)(?=')"

#make new column to random_sample.csv
df1['question'] = np.nan

for i in range(len(df1)):
    print(df1['goc'][i] + " " + str(i))
    for j in range(len(df2)):
        answers = re.findall(pattern, df2['answers'][j])
        for answer in answers:
            if answer == df1['goc'][i]:
                if pd.isna(df1['question'][i]):
                    df1['question'][i] = df2['question'][j]
                else:
                    df1['question'][i] = df1['question'][i] + " " + df2['question'][j]
                break

print(df1.head())
df1.to_csv("random_sample_merge_question.csv", index=False)