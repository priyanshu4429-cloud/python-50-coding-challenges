# HackerRank - Filter and Reduce
# Topic: Functional | Difficulty: Easy

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda a, b: a * b, fracs)
    return t.numerator, t.denominator

n = int(input())
fracs = [Fraction(*map(int, input().split())) for _ in range(n)]
result = product(fracs)
print(*result)
