num = input("Enter your numner: ")
reversed_num = 0

while num!= 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit 
    num //=10

print("Reversed number: " + num(reversed_num))
