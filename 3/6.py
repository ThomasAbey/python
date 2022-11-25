#Write a Python program to read a file line by line store it into a variable
with open ("test.txt","r") as fname:
    f = fname.readlines()
print(f)