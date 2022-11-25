#Ask the user for a string and print out whether this string is a palindrome or not


def isPalindrome(string):
    if(string==string[::-1]):
        return "The string is a palindrome"
    else:
        return "The string is not a palindrome"

string = input("Enter a string : ")
print(isPalindrome(string))            