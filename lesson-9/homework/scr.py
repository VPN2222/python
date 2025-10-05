class a:
    def __init__(self,radius):
        import math
        self.radius=radius
        self.perimeter = 2 * math.pi * radius
        
b=a(5)
print(b.radius)
print(b.perimeter)

class Person:
    from datetime import date
    def __init__(self,name,age,databirth):
        self.name=name
        self.age=age
        self.databirth=databirth
        def get_age(self):
         current_year = date.today().year
         return current_year - self.birth_year
     
p1 = Person("Abbos", "Uzbekistan", 2005)

print("Name:", p1.name)
print("Country:", p1.country)
print("Age:", p1.get_age())

class Calculate:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "0 ga bolish mumkin emas!"

calc = Calculate(10, 5)

print("Qoshish:", calc.add())
print("Ayirish:", calc.subtract())
print("Kopaytirish:", calc.multiply())
print("Bolish:", calc.divide())


import math
class Shape:
    def area(self):
        pass  
    def perimeter(self):
        pass  
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2  
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle Area:", round(circle.area(), 2), "Perimeter :", round(circle.perimeter(), 2))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)


bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)

print(bst.search(6))   # True
print(bst.search(7))   # False


class Stack:
    def __init__(self):
        self.items = []  
    def push(self, item):
        """Stackning ustiga element qoshish"""
        self.items.append(item)
    def pop(self):
        """Stackdan eng oxirgi elementni olish (va ochirish)"""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bosh!"
    def peek(self):
        """Eng oxirgi elementni korish (ochirmasdan)"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bosh!"
    def is_empty(self):
        """Stack bosh yoki yoqligini tekshirish"""
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack ichida:", s.items)
print("Eng yuqorisi:", s.peek())

print("Pop qildik:", s.pop())
print("Pop qildik:", s.pop())

print("Hozir stack:", s.items)
print("Boshmi?", s.is_empty())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

lst = LinkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.display()
lst.delete(20)
lst.display()


class ShoppingCart:
    def __init__(self):
        self.items = {} 
    def add_item(self, item, price):
        self.items[item] = price
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    def total_price(self):
        return sum(self.items.values())
    def display(self):
        for item, price in self.items.items():
            print(f"{item}: ${price}")
        print("Jami:", self.total_price())


 
cart = ShoppingCart()
cart.add_item("Apple", 2)
cart.add_item("Banana", 1)
cart.display()
cart.remove_item("Apple")
cart.display()


class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack bosh!"
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        print("Stack:", self.items)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue bosh!"
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        print("Queue:", self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} som qoshildi. Yangi balans: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} som yechildi. Qolgan balans: {self.balance}")
        else:
            print("Balans yetarli emas!")
    def display(self):
        print(f"Mijoz: {self.name}, Balans: {self.balance}")


user = BankAccount("Abbos", 5000)
user.deposit(2000)
user.withdraw(3000)
user.display()
