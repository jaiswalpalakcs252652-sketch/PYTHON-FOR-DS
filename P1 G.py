num = [20, 60, 80, 100, 10, 30, 50, 70, 16, 21]

print("List =", num)
print("Maximum =", max(num))
print("Minimum =", min(num))
print("Average =", sum(num) / len(num))

num.sort()
print("Ascending Order =", num)

num.sort(reverse=True)
print("Descending Order =", num)

num.append(60)
print("After Adding =", num)

num.pop(0)
print("After Removing First Item =", num)
