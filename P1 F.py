z = input("Enter a sentence: ")

words = len(z.split())
characters = len(z)

print("Number of words =", words)
print("Number of characters =", characters)
print("Lowercase =", z.lower())
print("Uppercase =", z.upper())
print("With underscores =", z.replace(" ", "_"))
