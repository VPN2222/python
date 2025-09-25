def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    res, c = "", 0
    for i, ch in enumerate(txt):
        res += ch; c += 1
        if c == 3:
            if ch in vowels or (i+1 < len(txt) and txt[i+1] == "_"):
                if i+1 < len(txt)-1: res += "_"
            elif i < len(txt)-1: res += "_"
            c = 0
    return res
output = insert_underscores("abcdefghij")
print(output)   

n=5
for i in range(n):
    print(i*i)


n = 5
i = 1
while i <= n:         
    j = 1
    while j <= i:     
        print(j, end=" ")
        j += 1
    print()           
    i += 1


n = 10
print("Sum is:", n * (n + 1) // 2)


for i in range(1, 11):  
    print(n * i)


numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i in(75,150,145):
        print(i)
        
        
        
num = 75869
print(len(str(num)))

n = 5
i = n
while i >= 1:           
    j = i
    while j >= 1:       
        print(j, end=" ")
        j -= 1
    print()             
    i -= 1
    
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
  print(i)
  
n = -10
for i in range(n, 0): 
    print(i)
    
for i in range(5):
    print(i)
    if i == 4:
        print('Done!')

for i in range(25,50):
      if all(i % j for j in range(2, int(i**0.5) + 1)):
        print(i)
        
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

import math
print(math.factorial(5))


def uncommon(list1, list2):
    return [x for x in list1 if x not in list2] + [y for y in list2 if y not in list1]

print(uncommon([1, 1, 2], [2, 3, 4]))        # [1, 1, 3, 4]
print(uncommon([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]
print(uncommon([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]

