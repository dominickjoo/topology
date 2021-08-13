import math
import itertools
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

# Returns the power set of a given iterable WITHOUT the empty set
def power_set(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))