#Write a Python program to convert unix timestamp string to readable date


import datetime
print ("Date : ",datetime.datetime.fromtimestamp(int("1668147585")).strftime("%B,%d,%Y") )


