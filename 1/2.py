#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num =int(input("Enter a number to test whether it is odd or even:"))
if(num==0):
    print("number is zero")
elif(num%2 ==0):
    print("This is an even number")
else:
    print("This is an odd number ")