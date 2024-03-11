#python script to find the sum of first n natural no.
num = int(input("Enter nth term: "))
sum = 0
for i in range(num + 1):
    sum += i
print(sum)