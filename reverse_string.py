s = "hello"
chars = list(s)

left = 0
right = len(s) - 1
while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1

result = "".join(chars)
print(result)
