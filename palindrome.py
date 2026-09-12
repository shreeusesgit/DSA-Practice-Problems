#To check if a string is palindrome

string = input("Enter a string:")

reverse = string[::-1]
if string == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
