# HackerRank - Reduce Function
# Topic: Functional | Difficulty: Easy

from functools import reduce

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

n = int(input())
nums = list(map(int, input().split()))
print(reduce(lcm, nums))
