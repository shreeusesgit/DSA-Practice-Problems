string  = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
    
print("Duplicate characters")
for char in frequency:
    if frequency[char] > 1:
        print(f"{char}: {frequency[char]}")