num = int(input("Enter the number to display table: "))
n = int(input("Enter your choice: "))
table = [num * n for n in range(1,n+1)]
print(table)

print("table with lambda function")

num = int(input("Enter a number: "))
table = [(lambda x: x * i)(num) for i in range(1, 11)]
print(table)