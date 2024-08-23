import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_questions.csv")
df1 = pd.read_csv("merge_final.csv")
# check the distribution of question types
print(df['question_type'].value_counts())
print(df['question_type'].value_counts(normalize=True) * 100)
print(df1['question_type'].value_counts())
print(df1['question_type'].value_counts(normalize=True) * 100)

# Plot the distribution of question id
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df['question_type'].value_counts().plot(kind='bar', title='Filtered Questions')
plt.subplot(1, 2, 2)
df1['question_type'].value_counts().plot(kind='bar', title='Merged Questions')


# Check percent of sentences of each type
print(df['answer_type'].value_counts())
print(df['answer_type'].value_counts(normalize=True) * 100)
print(df1['answer_type'].value_counts())
print(df1['answer_type'].value_counts(normalize=True) * 100)

# Plot the distribution of answer types
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df['answer_type'].value_counts().plot(kind='bar', title='Filtered Questions')
plt.subplot(1, 2, 2)
df1['answer_type'].value_counts().plot(kind='bar', title='Merged Questions')
plt.show()
