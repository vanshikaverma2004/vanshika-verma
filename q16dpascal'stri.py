n=int(input("enter the numbers of rows: "))
coef=1

for i in range(1, n+1):
    for space in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print (coef, end = " ")
    print()