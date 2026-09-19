# HackerRank - Symmetric Difference
# Topic: Sets | Difficulty: Easy

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
result = sorted(a.symmetric_difference(b))
print('\n'.join(map(str, result)))
