import pandas as pd

data = {
    "Name": ["Ram","Sam","Mira","Rita","John"],
    "Marks": [50, 80, 75, None, 90]
}

df = pd.DataFrame(data)

# Q1 Show first 3 rows

print("Q1:\n", df.head(3))

# Q2 Fill missing marks with mean

df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print("\nQ2:\n", df)

# Q3 Students with marks >70

print("\nQ3:\n", df[df["Marks"]>70])

# Q4 Add Grade column

df["Grade"] = ["C","B","B","B","A"]
print("\nQ4:\n", df)

# Q5 Describe data

print("\nQ5:\n", df.describe())
