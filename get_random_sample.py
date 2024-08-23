import pandas as pd

df = pd.read_csv("dang_dich.csv")
# drop column 2
df = df.drop(df.columns[2], axis=1)
print(df)
# get 500 random sample which have data in both not NaN
df = df.dropna()

df = df.sample(n=500, random_state=1)

# Save the filtered DataFrame to a new csv file
df.to_csv('random_sample.csv', index=False)



