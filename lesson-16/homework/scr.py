import numpy as np

lst = [12.23, 13.32, 100, 36.32]
print("Original List:", lst)

arr = np.array(lst)
print("One-dimensional NumPy array:", arr)

 

 
arr = np.arange(2, 11).reshape(3, 3)

print(arr)

 
arr = np.zeros(10)
print("Original vector:")
print(arr)
 
arr[6] = 11
print("\nUpdated vector:")
print(arr)

arr = np.arange(12, 38)
print(arr)

celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
 
fahrenheit = (celsius * 9/5) + 32

print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

 
arr = np.array([10, 20, 30])
print("Original array:", arr)
 
new_values = [40, 50, 60, 70, 80, 90]
 
result = np.append(arr, new_values)

print("After append values to the end of the array:", result)

 
arr = np.random.randint(1, 100, 10)
print("Random array:", arr)

# Calculate statistical values
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

 
rr = np.random.random((10, 10))
print("10x10 Random Array:\n", rr)
 
min_val = np.min(rr)
max_val = np.max(rr)

print("\nMinimum value:", min_val)
print("Maximum value:", max_val)

arr = np.random.random((3, 3, 3))

print("3x3x3 Random Array:\n", arr)
