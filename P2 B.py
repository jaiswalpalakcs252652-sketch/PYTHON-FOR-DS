# Question 1: Tuple Operations in Python


tuple1 = (22, 33, 46, 67, 78, 30)
print("\na. Tuple:", tuple1)


print("\nb. First Element:", tuple1[0])
print("   Last Element:", tuple1[-1])


print("\nc. Middle 3 Elements:", tuple1[1:4])


tuple2 = (65, 78, 80, 99, 67, 88, 56, 41, 14)
concat_tuple = tuple1 + tuple2
print("\nd. Concatenated Tuple:", concat_tuple)


reversed_tuple = tuple1[::-1]
print("\ne. Reversed Tuple:", reversed_tuple)


tuple3 = (1, 2, 3, 2, 4, 2, 5, 2, 4, 5, 6, 2, 3 , 4, 6, 4, 8)
count_element = tuple3.count(4)
print("\nf. Count of 4:", count_element)


index_element = tuple1.index(30)
print("\ng. Index of 30:", index_element)


element = 40
if element in tuple1:
    print("h.", element, "exists in the tuple.")
else:
    print("h.", element, "does not exist in the tuple.")


num_list = [100, 200, 300, 400]
tuple_from_list = tuple(num_list)
print("\ni. Tuple from List:", tuple_from_list)


unsorted_tuple = (56, 2, 88, 12, 99, 35, 90, 67, 79, 45, 87)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("\nj. Sorted Tuple:", sorted_tuple)


repeated_tuple = tuple1 * 3
print("\nk. Repeated Tuple:", repeated_tuple)


print("\nl. Checking Tuple Immutability:")
try:
    tuple1[0] = 100
except TypeError as e:
    print("   Error:", e)
    print("   Tuples are immutable and cannot be modified.")
