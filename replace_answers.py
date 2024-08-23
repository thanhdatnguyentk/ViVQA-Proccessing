import pandas as pd
import re
pd.SettingWithCopyWarning = False
df = pd.read_csv("filtered_questions.csv")
df1 = pd.read_csv("answer_set3_new.csv")

#fill nan value in df2 by ''
df1 = df1.fillna('')

pattern = "(?<=answer':\s')(?:[^']+|\s+)(?=')"

for i in range(len(df)):
    answers = re.findall(pattern, df['answers'][i])
    for answer in answers:
        if answer in df1['0'].values:
            #process answer
            answer_process = 'answer\': \'' + answer + '\''
            value = df1['1'][df1['0'] == answer].values[0]
            if value != '':
                df['answers'][i] = re.sub(answer_process,'answer\': \'' + value + '\'', df['answers'][i])

df.to_csv("test_5.csv", index=False)