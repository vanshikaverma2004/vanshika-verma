def greater_than(x, y):
    return x>y

def less_than(x, y):
    return x<y

def greater_than_equal_to(x, y):
    return x>=y

def less_than_equal_to(x, y):
    return x<=y

print("Select operation.")
print("1.Greater Than.")
print("2.Less Than.")
print("3.Greater Than Equal To.")
print("3.Less Than Equal To.")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please a number. ")
            continue
        if choice=='1':
            print(num1, ">", num2, "=", greater_than(num1, num2))

        if choice=='2':
            print(num1, "<", num2, "=", less_than(num1, num2))

        if choice=='3':
            print(num1, ">=", num2, "=", greater_than_equal_to(num1, num2))

        if choice=='4':
            print(num1, "<=", num2, "=", less_than_equal_to(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
else:
    print("Invalid Input")
