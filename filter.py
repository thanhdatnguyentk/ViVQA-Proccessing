import pandas as pd


df = pd.read_csv("merge_final.csv")

# Check the number of sentences of each type
print(df['question_type'].value_counts())

# Get each type 7.6 percent of the total number of types 
df_filtered = df.groupby('question_type').apply(lambda x: x.sample(frac=0.076))

# Check the number of sentences of each type after filtering
print(df_filtered.shape)
print(df_filtered['question_type'].value_counts())

# Save the filtered DataFrame to a new csv file
df_filtered.to_csv('filtered_questions.csv', index=False)
