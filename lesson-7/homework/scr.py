def is_prime(n):
  if n/2==0:
    print('False')
  else:
    print('True')
    
print(is_prime(3))



def digit_sum(k):
    s = 0
    while k > 0:
        s += k % 10
        k //= 10
    return s   
print(digit_sum(24))



def son_multiple(n:int):
    a=[]
    k=1
    while 2**k <=n:
        a.append(2**k)
        k += 1
    return a

print(son_multiple(10))
