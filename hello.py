def rotate(nums, k):
    n = len(nums)
    k %= n

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])


# Input
nums = [1, 2, 3, 4, 5, 6, 7]
k = 4
# Rotate the array
rotate(nums, k)
\
# Output
print("Rotated array:", nums)