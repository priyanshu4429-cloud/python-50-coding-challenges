# HackerRank - Set Mutations
# Topic: Sets | Difficulty: Easy

n = int(input())
a = set(map(int, input().split()))
b = int(input())
for _ in range(b):
    cmd = input().split()
    op, vals = cmd[0], set(map(int, input().split()))
    if op == 'intersection_update': a.intersection_update(vals)
    elif op == 'update': a.update(vals)
    elif op == 'difference_update': a.difference_update(vals)
    elif op == 'symmetric_difference_update': a.symmetric_difference_update(vals)
print(sum(a))
