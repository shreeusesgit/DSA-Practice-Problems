string1 = input("Enter first string:")
string2 = input("Enter second string:")

if sorted(string1) == sorted(string2):
    print("It is a anagram")
else:
    print("It is not a anagram")
    