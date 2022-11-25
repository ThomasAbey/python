#Write a Python program to get the file size of a plain file

def file_size(f):
    import os 
    statinfo =os.stat(f)
    return statinfo.st_size
print("File size of a plain file", file_size("list.txt"))    