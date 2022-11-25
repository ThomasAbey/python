#Write a program that asks the user to enter their name and their age. 
#Print out a message that greets them and that tells them the year that they will turn 100 years old.


from datetime import datetime
name = input("Enter your name : ")
age = int(input("Enter your age : "))
year = int((100-age) + datetime.now().year)
print(name + "you will be 100 year old in " +str(year))