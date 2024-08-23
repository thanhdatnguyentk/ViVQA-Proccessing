import json 
import pandas as pd

df1 = pd.read_csv("merged_annotations.csv")
df2 = pd.read_csv("merged_questions.csv")

df3 = pd.merge(df1, df2, on="question_id")

df3.to_csv("merge_final.csv", index=False)

print(df3.head())
print(df3.shape)