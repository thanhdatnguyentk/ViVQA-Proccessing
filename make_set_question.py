import pandas as pd
import re
df = pd.read_csv("data/filtered_questions.csv")

#make set of question

question_set = set()
for i in range(len(df)):
    question_set.add(df['question'][i])
    
#save set to file csv
df = pd.DataFrame(question_set)
df.to_csv("question_all_set.csv", index=False)
print(question_set)
print(len(question_set))