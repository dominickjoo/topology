import math
from functools import reduce

# Returns True if given number is prime, else False
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

# Returns the greatest common divisor of all the integers in the given list
def gcd_mult(nums):
    return reduce(math.gcd, nums)