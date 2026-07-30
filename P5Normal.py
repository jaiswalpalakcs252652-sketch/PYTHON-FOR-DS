import pandas as pd

data1 = {
    "Name": ["Palak", "Riya", "Aman"],
    "Age": [20, 19, 21],
    "Marks": [85, 90, 88]
}

df1 = pd.DataFrame(data1)
print("5(a)")
print(df1)

data2 = {
    "Age": [20, 19, 21, 22, 20],
    "Marks": [85, 90, 88, 92, 87]
}

df2 = pd.DataFrame(data2)
print("\n5(b)")
print(df2)
print(df2.describe())

data3 = {
    "Math": 85,
    "Science": 90,
    "English": 88,
    "Computer": 95
}

series1 = pd.Series(data3)
print("\n5(c)")
print(series1)

series2 = pd.Series([10, 20, 30, 40, 50])
filtered_series = series2[series2 > 25]

print("\n5(d)")
print(series2)
print(filtered_series)
