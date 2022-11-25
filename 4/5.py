#Write a Python program to get days between two dates. Go to the editor 
#Exampe: days between 28/02/2000 and  28/02/2001


from datetime import date
d1 = date(year=2001, month=2,day=28)
d2 = date(year=2000, month=2, day=28)
d3 = d1 - d2
print(d3)

