import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
 
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})

 
print(df.head(3))
 
print("Mean age:", df['age'].mean())
 
print(df[['first_name', 'City']])
 
df['Salary'] = np.random.randint(3000, 8000, size=len(df))
 
print(df.describe())

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
 
sales_and_expenses = pd.DataFrame(data)

 
print("Jadval:")
print(sales_and_expenses)
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print("Eng katta savdo (max sales):", max_sales)
print("Eng katta xarajat (max expenses):", max_expenses)

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print("Eng kichik savdo (min sales):", min_sales)
print("Eng kichik xarajat (min expenses):", min_expenses)

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print("Ortacha savdo (average sales):", avg_sales)
print("Ortacha xarajat (average expenses):", avg_expenses)


data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

 
expenses = pd.DataFrame(data)

 
expenses = expenses.set_index('Category')

max_expense = expenses.max(axis=1)
min_expense = expenses.min(axis=1)
avg_expense = expenses.mean(axis=1)
 
print("Maximum expense for each category:")
print(max_expense)
print("Minimum expense for each category:")
print(min_expense)
print("Average expense for each category:")
print(avg_expense)
