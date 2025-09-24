def is_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2000))  
print(is_leap_year(1900))

n=int(input('Son kiriting'))
if n % 2 != 0:
    print('Weird')
elif n%2==1 and 2 <= n <= 5:
    print('not')
elif n%2==0 and 6 <= n <= 20:
    print('weird')
elif n % 2 == 0 and n > 20:
    print('Not weird')
    
a = int(input("a = "))
b = int(input("b = "))

print(list(range(a + a%2, b+1, 2)))
