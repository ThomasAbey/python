#Write a Python program to count the number of lines in a text file.


def file_length(f):
    with open ("test.txt") as f:
        for i,l in enumerate(f):
            pass    
    return i +1
print(file_length("test.txt"))        