# HackerRank - Maximize It!
# Topic: Itertools | Difficulty: Easy

from itertools import product

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]
print(max(sum(x**2 for x in combo) % m for combo in product(*lists)))
