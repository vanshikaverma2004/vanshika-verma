#python program to print all the palindrome number in the range of 500-1000
minvalue = int(input("Enter minvalue: ")) 
maxvalue = int(input("Enter maxvalue: "))
print("Palindrome number between", minvalue, maxvalue, "are: ")
for num in range(minvalue, maxvalue+1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp  = temp // 10
        
    if(num == reverse):
        print(num)