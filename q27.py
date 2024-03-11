num = int(input("Enter the number for check the divisibility: "))
div = int(input("Enter the number with which divisibility need to be check: "))
if num % div == 0:
    print("The number is divisible..")
else:
    print("The number is not divisible..")
    
"""lambda function

list = [13, 14, 87, 44, 70, 09]
result = list(filter(lambda x: (x % 7 == 0). list))
print("Number that are divisible by 7 are:", result)"""