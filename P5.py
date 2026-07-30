import pandas as pd
df = pd.read_csv("palak.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nShape of the dataset:")
print(df.shape)




import pandas as pd
df = pd.read_csv("palak.csv")
print(df.describe())
print("\nDataset Information:")
print(df.info())




import pandas as pd
student_data = {
    "anxiety_level": 14,
    "self_esteem": 20,
    "depression": 11,
    "stress_level": 1
}
s = pd.Series(student_data)
print(s)





import pandas as pd
stress = pd.Series([14, 15, 12, 16, 16, 20, 4, 17, 13, 6])
print("Original Series:")
print(stress)
filtered = stress[stress > 15]






print("\nValues greater than 15:")
print(filtered)
