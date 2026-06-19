count = 0

print("Squares of numbers from 1 to 10:")

for z in range(1, 11):
    print(z, "=", z * z)

for z in range(5):
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        count = count + 1

print("Number of even numbers =", count)
