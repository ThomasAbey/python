#Take the following lists

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.



a = [1, 1, 2, 3, 5, 8, 13, 21,1, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result1 = [] 
result2 = []
[result1.append(x) for x in a if x not in result1] 
[result2.append(y) for y in b if y not in result2 ]

print(result1)   
print(result2)      