import pandas as pd

df = pd.read_csv("filtered_questions.csv")

#make set of answer
answer_set = set(df['multiple_choice_answer'])

#save set to file csv
df = pd.DataFrame(answer_set)
df.to_csv("answer_set.csv", index=False)

#display size of set
print(answer_set)
print(len(answer_set))