def swap_list(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

cars = ["Porsche", "MacLaren", "BMW", "Lamborghini", "G-Wagon", "Buggati"]

print("LIST :", cars)

swap1 = 1
swap2 = 4

new_list = swap_list(cars, swap1, swap2)

print("NEW LIST :", new_list)
