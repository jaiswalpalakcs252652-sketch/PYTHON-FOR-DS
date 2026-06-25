#2a. Write a python code to create nested tuples.
tuple1 = ("Python for Data Science", 301)
tuple2 = ("Operating System", 302)
tuple3 = ("Scala for Data Science", 303)
tuple4 = ("TOC", 304)
tuple5 = ("DS", 305)
tuple6 = ("FP", 306)
nested_tuple = (tuple1, tuple2, tuple3, tuple4, tuple5, tuple6)
print("Nested Tuple:", nested_tuple)


print("Four subject tuple:", nested_tuple[3])
print("Name of first subject:", nested_tuple[0][0])


print("Last subject tuple (negative index):", nested_tuple[-1])
print("Name of last subject:", nested_tuple[-1][0])


print("\nAll Subjects:")
for subject in nested_tuple:
    print(f"Subject Name: {subject[0]}, Code: {subject[1]}")


reversed_tuple = nested_tuple[::-1]
print("\nReversed Tuple:", reversed_tuple)


sliced_tuple = nested_tuple[0:3]
print("Sliced Tuple (first three subjects):", sliced_tuple)


tuple7 = ("Hindi", 307)
updated_tuple = nested_tuple + (tuple7,)
print("After Concatenation:", updated_tuple)


try:
    nested_tuple[0][1] = 999 
except TypeError as e:
    print("\nTuple Immutability Test: Error occurred ->", e)


#2b. Write a python code to sort the nested tuple using sorted() function.
nested_tuple = (
("Python for Data Science", 301),
("Operating System", 302),
("Scala for Data Science", 303),
("TOC", 304),
("DS", 305),
("FP", 306),
)

sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])

print("Sorted Subjects (by subject code):", sorted_subjects)


#2c. Write a python code to copy or clone list.
original_list = ["Python", "OS", "Scala", "CN"]

copy11 = original_list[:]
copy12 = original_list[1:3]
copy13 = original_list[:-1]


copy22 = list(original_list)

copy33 = original_list.copy()

print("Original List:", original_list)
print("Copy using slicing:", copy11)
print("Copy using slicing:", copy12)
print("Copy using slicing:", copy13)
print("Copy using list():", copy22)
print("Copy using copy():", copy33)


#2d.Write a python code to check immutability property of python tuples.

subject = ("Python for Data Science", 301)

try:
    subject[1] = 301 
except TypeError as e:
    print("Tuple is immutable! Error:", e)

    
