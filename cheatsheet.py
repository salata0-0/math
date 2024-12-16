# Week 1: Introduction
# Basic commands and syntax
print("Hello, World!")  # Printing output
x = 5 + 3  # Assignment
print("x =", x)  # Using arguments in print()
print(type(x))  # Type checking

# Week 2: Variables and Types
x = 42
pi = 3.14
message = "Hello"
print(len(message))  # String length

# Type casting
x_str = str(x)
print("x as string:", x_str)

# Casting float to int and vice versa
pi_as_int = int(pi)
print("pi as int:", pi_as_int)
x_as_float = float(x)
print("x as float:", x_as_float)

print("Max of 5, 10:", max(5, 10))

# Additional numeric operators
print("Modulus 10 % 3:", 10 % 3)
print("Floor division 10 // 3:", 10 // 3)

# Math functions
import math
print("Pi is:", math.pi)
print("sin(pi/2):", math.sin(math.pi / 2))
print("Square root of 16:", math.sqrt(16))
print("Exponential e^2:", math.exp(2))

# Week 3: Conditionals
age = 18
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")

# Comparison operators
print(10 == 10)  # True
print(10 != 5)  # True
print(10 > 5)  # True
print(10 < 15)  # True
print(10 >= 10)  # True
print(10 <= 20)  # True

# Logical operators
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# Week 4: Loops
for i in range(5):
    print("Iteration:", i)

for char in "hello":
    print("Character:", char)

counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1

# Breaking and continuing loops
for i in range(10):
    if i == 5:
        break
    print("Looping:", i)

# Week 5: Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def square(x):
    return x ** 2

print("Square of 3:", square(3))

# Void function

def shout():
    print("Hello!")

shout()

# Week 6: Lists
nums = [1, 2, 3, 4]
nums.append(5)
print("List after append:", nums)
nums.sort()
print("Sorted list:", nums)
nums.insert(2, 99)
print("List after insertion:", nums)

# List slicing
print("First two elements:", nums[:2])
print("Last element:", nums[-1])

# Week 7: Strings
text = "Hello World"
print(text.upper())
print("Found index:", text.find("World"))
print("Substring:", text[0:5])
print("Replace:", text.replace("World", "Python"))

# String methods
print(text.isalpha())  # Check if all characters are alphabets
print(text.startswith("Hello"))
print(text.endswith("!"))

# String formatting
name = "Alice"
age = 25
print(f"{name} is {age} years old.")

# Week 8: Dictionaries and Tuples
person = {"name": "Alice", "age": 25}
print("Person's name:", person["name"])
person["city"] = "Wonderland"
print("Updated dictionary:", person)

# Traversing a dictionary
for key, value in person.items():
    print(key, ":", value)

def info():
    return "Alice", 25

name, age = info()
print("Tuple unpacked:", name, age)

# Week 9: Files
import os
cwd = os.getcwd()
print("Current directory:", cwd)
file_path = os.path.join(cwd, "example.txt")

with open(file_path, "w") as file:
    file.write("Hello, file!")

with open(file_path, "r") as file:
    content = file.read()
    print("File content:", content)

# File reading methods
with open(file_path, "r") as file:
    print("Readlines:", file.readlines())
    file.seek(0)
    print("Read:", file.read())

# Week 10: Classes I
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Rex")
d.bark()

# Week 11: Classes II
class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal):
    def sound(self):
        return "Meow"

c = Cat()
print("Cat sound:", c.sound())

# Overriding and overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print("Point addition result:", result.x, result.y)

# Week 12: NumPy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt

array = np.array([1, 2, 3])
print("Array + 1:", array + 1)

# NumPy operations
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:", matrix)
print("Matrix transpose:", matrix.T)
print("Mean of array:", np.mean(array))

# Line plot
plt.plot(array, array**2)
plt.title("Quadratic Plot")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.show()

# Scatter plot
plt.scatter(array, array**2, color='red')
plt.title("Quadratic Scatter Plot")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.show()

# Bar plot
plt.bar(array, array**2, color='blue')
plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.show()

# Week 13: Modules
from math import sqrt
print("Square root of 16:", sqrt(16))

# Importing custom modules
# Assume mymodule.py exists with a function greet()
# from mymodule import greet
# print(greet("Bob"))
