# HackerRank - Check Strict Superset
# Topic: Sets | Difficulty: Easy

a = set(map(int, input().split()))
n = int(input())
result = all(a.issuperset(set(map(int, input().split()))) for _ in range(n))
print(result)
