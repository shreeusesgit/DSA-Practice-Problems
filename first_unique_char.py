string = "swiss"

frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

for char in string:
    if frequency[char] == 1:
        print(char)
        break
