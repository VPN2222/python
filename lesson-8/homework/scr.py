def assd():
    try:
        a = 10 / 0
    except ZeroDivisionError:
        print('0 ga bolish mumkin emas')

def assd():
     try:
       number = int(input("son kiritng: "))
       print(f"You entered: {number}")
     except ValueError:
       print("son kiritng harif emas")


try:
    with open("example.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")


try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    if not (x.isdigit() and y.isdigit()):
        raise TypeError("Inputs must be numerical!")
    x, y = int(x), int(y)
    print(f"Sum = {x + y}")
except TypeError as e:
    print("hatto", e)


try:
    with open("secret.txt", "w") as f:  
        f.write("Test")
except PermissionError:
    print("Permission denied!")
    
        
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except KeyboardInterrupt:
    print("Input cancelled by user")
   
try:
    a, b = 10, 0
    print(a / b)
except ArithmeticError as e:
    print("Arithmetic error:", e)

try:
    my_list = [1, 2, 3]
    my_list.push(4)  
except AttributeError:
    print("Attribute does not exist!")


with open("test.txt", "r") as f:
    print(f.read())

n = 3
with open("test.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

with open("test.txt", "a") as f:
    f.write("\nNew line added")
with open("test.txt", "r") as f:
    print(f.read())


n = 3
with open("test.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

with open("test.txt", "r") as f:
    lines = f.readlines()
print(lines)

text = ""
with open("test.txt", "r") as f:
    for line in f:
        text += line
print(text)

arr = []
with open("test.txt", "r") as f:
    for line in f:
        arr.append(line.strip())
print(arr)

with open("test.txt", "r") as f:
    words = f.read().split()
print(max(words, key=len))

with open("test.txt", "r") as f:
    print(len(f.readlines()))

from collections import Counter
with open("test.txt", "r") as f:
    words = f.read().replace(",", " ").split()
print(Counter(words))

import os
print(os.path.getsize("test.txt"), "bytes")

items = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as f:
    for item in items:
        f.write(item + "\n")

with open("test.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

import random
with open("test.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))

with open("test.txt") as f:
    lines = [line.strip() for line in f]
print(lines)

with open("test.txt", "r") as f:
    words = f.read().replace(",", " ").split()
print("Word count:", len(words))

chars = []
with open("test.txt", "r") as f:
    for line in f:
        chars.extend(list(line.strip()))
print(chars)

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is {letter}.txt\n")

import string
n = 5  
letters = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")

