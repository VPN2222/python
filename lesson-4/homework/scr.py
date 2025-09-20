d = {"apple": 10, "banana": 2, "cherry": 7, "mango": 5} 
print("Ascending:", dict(sorted(d.items(), key=lambda x: x[1])))
print("Descending:", dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))

b={0: 10, 1: 20}
b[0] = 1    
b[1] = 20    
b[2] = 30 
print(b)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

n=5
d={x:x*x for x in range(1,n+1)}
print(d)

d = {x: x*x for x in range(1, 16)}
print(d)

d = {'Name', 'Jahongir', 'Last name', 'Abu', 'Age', '32'}
print(d)
print(type(d))

s = {"apple", "banana", "cherry", "mango"}
print(sorted(s))

members = {"Ali", "Vali", "Hasan", "Husan"}
members.add('Akber')
print(members)

s = {"apple", "banana", "cherry", "mango"}
s.remove('apple')
print(s)



s = {"apple", "banana", "cherry", "mango"}
s.discard('banana')
s.discard('cherry')
print(s)
