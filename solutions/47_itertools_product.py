# HackerRank - itertools.product()
# Topic: Itertools | Difficulty: Easy

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a, b))
