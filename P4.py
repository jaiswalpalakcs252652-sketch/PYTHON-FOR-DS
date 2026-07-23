import numpy as np
print("Palak Jaiswal S089")
print("4a. Create a NumPy Array")
arr1 = np.array([89, 16, 21, 10, 88])
print("NumPy Array:", arr1)
print()


print("4b. Basic Operations on a Single Array")
print("Original Array:", arr1)
print("Addition (+5):", arr1 + 5)
print("Subtraction (-5):", arr1 - 5)
print("Multiplication (*2):", arr1 * 2)
print("Division (/2):", arr1 / 2)
print()


print("4c. Array Slicing")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Array:", arr2)
print("Elements from 1st to 5th:", arr2[0:5])
print()


print("4d. Alphabetical Sorting")
arr3 = np.array(["Orange", "Apple", "Banana", "Mango"])
sorted_arr = np.sort(arr3)
print("Original Array:", arr3)
print("Sorted Array:", sorted_arr)
print()


print("4e. Filter Maximum Value")
arr4 = np.array([12, 45, 67, 23, 89, 34, 89])
max_value = np.max(arr4)
filter_arr = arr4[arr4 == max_value]
print("Original Array:", arr4)
print("Maximum Value:", max_value)
print("Filtered Array:", filter_arr)
