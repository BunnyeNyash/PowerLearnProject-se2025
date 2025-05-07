import pandas as pd

# DataFrame with 3 students: name, age, and grade.
data = {
    "Name": ["Alice", "Mark", "Bunnye"],
    "Age": [15, 14, 12],
    "Grade": [40, 90, 98]
}

df = pd.DataFrame(data)
print(df)


# Add a column called “Passed” where grade > 50 = True.
df["Passed"] = df["Grade"] > 50
print(f"\n{df}")

# Filter and display only students who passed.
passed_students = df[df["Passed"] == True]
print(f"\nstudents who passed:\n{passed_students}")
