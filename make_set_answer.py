import pandas as pd
import re
df = pd.read_csv("filtered_questions.csv")

#make set of each answer in answers column
answer_set = set()
patern = "(?<=answer':\s')(?:[^']+|\s+)(?=')"
for i in range(len(df)):
    answers = re.findall(patern, df['answers'][i])
    for answer in answers:
        answer_set.add(answer)

#save set to file csv
df = pd.DataFrame(answer_set)
df.to_csv("answer_all_set.csv", index=False)
print(answer_set)
print(len(answer_set))