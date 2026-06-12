# Python Operators

print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# Arithmetic Operators

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)



x = 12
y = 5

print(x / y)



x = 12
y = 5

print(x // y)

# Assignment Operators / The Walrus Operator

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# The Ternary Operator

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# Instead of Elif:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

# Comparison Operators

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining Comparison Operators

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

# Logical Operators

x = 5
print(x > 0 and x < 10))
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

# Membership Operators

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

# Membership in Strings

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Python Bitwise Operators

print(6 & 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the & operator compares the bits and returns 0010, which is 2 in decimal.

print(6 | 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the | operator compares the bits and returns 0111, which is 7 in decimal.

print(6 ^ 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.

# Operator Precedence

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# Left-to-Right Evaluation

print(5 + 4 - 7 + 3)
