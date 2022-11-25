#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right



import random
a =random.randint(1,9)
number = int(input("Guess the number between 1 to 9 : "))
if number>a:
    print("You guessed too high")

elif number<a:
    print("You guessed too low")

else:
    print("You guessed the right one")        