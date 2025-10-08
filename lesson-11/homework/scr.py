 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


 
def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

 
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

 
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    return "File written successfully!"


 
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found!"


 

print("==== Math Operations ====")
print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(2, 8))
print("Divide:", divide(12, 3))

print("\n==== String Utils ====")
print("Reversed:", reverse_string("hello"))
print("Vowel count:", count_vowels("education"))

print("\n==== Geometry ====")
print("Circle area:", calculate_area(5))
print("Circle circumference:", calculate_circumference(5))

print("\n==== File Operations ====")
write_file("test.txt", "Hello, Python Homework!")
print(read_file("test.txt"))
