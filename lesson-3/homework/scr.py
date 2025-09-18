fruits=['apple','banana','Mango','cherry','watermelon']
print('the third fruit',fruits[2])
numbers=[2,3,4,5]
numbers1=[1,4,7,8]
numbers.extend(numbers1)
print(numbers)

numbers = [10, 20, 30, 40, 50, 60, 70]
a=[numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(a)

movies=['eigth Miles','Warior','Gus with guns','asd','asdsas']
movie_tuple=tuple(movies)
print(movie_tuple)

city=['America','Greeck','India','Paris']
if 'Paris' in city:
    print("Paris in the list")
else:
    print('Paris is not in list')
    
numbers = [1, 2, 3, 4, 5, 6]
duplicate=numbers*2
print(duplicate)

numbers = [1, 2, 3, 4, 5, 6]
numbers[0],numbers[-1]=numbers[-1],numbers[0]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6,7,8]
slice_part=numbers[3:8]
print(slice_part)

colors = ["red", "blue", "green", "blue", "yellow", "blue", "black"]
print(colors.count('blue'))

animals = ("cat", "dog", "lion", "tiger", "elephant")
print(animals.index('lion'))


tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
b=tuple1+tuple2
print(b)

my_list = [10, 20, 30, 40, 50]
my_tuple = ("apple", "banana", "cherry", "mango")

print(len(my_list))
print(len(my_tuple))

my_tuple = ("apple", "banana", "cherry", "mango")
lis_a=list(my_tuple)
print(lis_a)

numbers=(2343,564334,877564,96752423,5473242)
print('Max',max(numbers))
print('Min',min(numbers))

words = ("apple", "banana", "cherry", "mango")
print(words[::-1])
