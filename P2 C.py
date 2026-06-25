# Question 2: List Operations in Python


nums = [12, 45, 7, 89, 23, 98, 67, 88, 90, 34, 45, 56, 78]
largest = max(nums)
print("\na. Largest Number:", largest)


list_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 5, 8, 9, 3, 4]
unique_list = list(set(list_with_duplicates))
print("\nb. List after removing duplicates:", unique_list)


nums2 = [10, 15, 20, 25, 30, 35, 40, 88, 5, 67, 45]
even_count = 0
for num in nums2:
    if num % 2 == 0:
        even_count += 1
print("\nc. Number of even elements:", even_count)


num_list = []
print("\nd. Enter 5 nums:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)
print("   List:", num_list)

def average(lst):
    return sum(lst) / len(lst)

sample_list = [10, 20, 30, 40, 50]
print("\ne. Average:", average(sample_list))


string = "Porsche"
char_list = list(string)
print("\nf. List of Characters:", char_list)


words = ["Hello", "Welcome", "To", "Porsche", "Showroom"]
joined_string = " ".join(words)
print("\ng. Joined String:", joined_string)
