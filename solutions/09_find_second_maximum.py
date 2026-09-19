# HackerRank - Find the Second Maximum Number in a List
# Topic: Lists | Difficulty: Easy

n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])
