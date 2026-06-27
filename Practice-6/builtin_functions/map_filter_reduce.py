from functools import reduce


digits = [1,2,3,4,5,6,7,8,9]

# Use map() and filter() on lists

squares = list(map(lambda x: x ** 2, digits))
print(squares)

evens = list(filter(lambda x: x % 2 == 0, digits))
print(evens)

# Aggregate with reduce() (from functools)

total = reduce(lambda x, y: x+y, digits)
print(total)

product = reduce(lambda x, y: x*y, digits)
print(product)
