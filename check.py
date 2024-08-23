import pandas


df = pandas.read_csv("filtered_questions.csv")
df1 = pandas.read_csv("merge_final.csv")
# Check percent of sentences of each type
print(df['answer_type'].value_counts())
print(df['answer_type'].value_counts(normalize=True) * 100)
print(df1['answer_type'].value_counts())
print(df1['answer_type'].value_counts(normalize=True) * 100)