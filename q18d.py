x= int(input("Enter nth digit: "))
def Fibo(a):
    if a<= 0:
        print("Incorrect input")
    elif a == 1:
        return 0
    elif a == 2:
        return 1
    else: 
        return Fibo(a-1)+Fibo(a-2)

print(Fibo(x))