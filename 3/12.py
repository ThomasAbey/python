#Write a Python program to write a list to a file.


names = ["Arun","Abin","Akash"]
with open ("list.txt","w+") as f:
    for items in names:
     f.write('%s\n' %items)
print("Done")