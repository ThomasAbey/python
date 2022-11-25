#Write a Python program to count the number of characters (character frequency) in a string.

test_str = "MASHUPSTACK"
freq = {}
for i in test_str:
    if i in freq:
        freq [i] +=1
    else:
        freq [i] =1
print(" the number of characters (character frequency) in a string" + str(freq))            