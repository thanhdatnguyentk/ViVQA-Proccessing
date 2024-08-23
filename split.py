import pandas as pd

df = pd.read_csv("answer_set.csv")



answer_set1 = pd.read_csv("answer_set1.csv")
answer_set2 = df.drop(answer_set1.index).sample(frac=0.5, random_state=1)
answer_set3 = df.drop(answer_set1.index).drop(answer_set2.index)

answer_set2.to_csv("answer_set2.csv", index=False)
answer_set3.to_csv("answer_set3.csv", index=False)

print(len(answer_set1), len(answer_set2), len(answer_set3))

print("Done splitting the dataset.")
