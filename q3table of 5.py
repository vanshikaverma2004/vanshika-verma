num = int(input("Display multiplication table of? : "))

n= int (input("enter last iteration: "))

for i in range (1, n+1):
    print (num, 'x', i, '=', num*i)

str = input("enter your string: ")

print("reversed string is: ", str[::-1])
