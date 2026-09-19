# HackerRank - Collections.Counter()
# Topic: Collections | Difficulty: Easy

from collections import Counter

x = int(input())
shoes = Counter(map(int, input().split()))
n = int(input())
total = 0
for _ in range(n):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        total += price
        shoes[size] -= 1
print(total)
