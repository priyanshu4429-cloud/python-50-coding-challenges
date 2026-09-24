# HackerRank - Set .union() Operation
# Topic: Sets | Difficulty: Easy

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.union(b)))
