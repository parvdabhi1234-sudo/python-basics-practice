import pandas as pd

# Create DataFrame

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, None, 70, 95],
    "Age": [20, 21, 19, 22, None]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

# head & tail

print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())

# info

print("\nInfo:")
print(df.info())

# describe

print("\nDescribe:\n", df.describe())

# Null values

print("\nNull values:\n", df.isnull().sum())

# Fill null

df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("\nAfter fillna:\n", df)

# Filtering

print("\nMarks > 80:\n", df[df["Marks"] > 80])

# Add column

df["Passed"] = df["Marks"] > 75
print("\nAdded column:\n", df)

# Drop column

df.drop("Passed", axis=1, inplace=True)

print("\nFinal DataFrame:\n", df)

print("\n--- Day 12 Pandas Complete ---")
