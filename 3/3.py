#Write a Python program to append text to a file and display the text.
f = open("test.txt","a")
f.write("Thank You")
f.close()
f = open("test.txt","r")
print(f.read())