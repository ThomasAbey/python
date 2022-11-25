#Write a Python program to read a file line by line store it into an array.
content_array = []
with open ("test.txt","r") as f:
    for x in f:
        content_array.append(x)
print(content_array)

