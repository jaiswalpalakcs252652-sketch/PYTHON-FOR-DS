import math
while True:
    try:
        n = input("Enter a number: ")
        if n == "exit":
            break
        n = float(n)
        s = math.sqrt(n)
        print("Square root =", s)
    except:
        print("Invalid Input")
