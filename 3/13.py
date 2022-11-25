#Write a Python program to copy the contents of a file to another file .
with open ("test.txt","r") as firstfile , open ("test1.txt","a") as secondfile:
    for f in firstfile:
     secondfile.write(f)