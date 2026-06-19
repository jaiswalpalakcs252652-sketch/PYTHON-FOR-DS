students = {
    "Sakshi": 80,
    "Nisha": 90,
    "Ram": 75,
    "Palak": 95,
    "Bhavesh": 85
}

print("Student Details:")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

print("Class Average =", average)

top_student = max(students, key=students.get)

print("Highest Marks Student =", top_student)
print("Marks =", students[top_student])
