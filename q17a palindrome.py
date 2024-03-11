#python script using function for finding the given no is palindrome or not
num = input("Enter  any number: ")
try:
    val = int(num)
    if num == str(num)[::-1]:
         print("The given no. is PALINDROME!!")
    else:
       print("The given no. is not a PALINDROME!!")
except ValueError:
    print("That's not a valid no.")
    
      