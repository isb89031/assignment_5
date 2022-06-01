def is_divisible_by_k(x, k):
    '''
    Checks whether x is divisible by k.
    '''
    return x % k == 0

# Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000
nums = []
for x in range(1, 1001):
    if is_divisible_by_k(x, 2) or is_divisible_by_k(x, 5) or is_divisible_by_k(x, 7):
        nums.append(x)

# Sum the corresponding integers
sum(nums)
