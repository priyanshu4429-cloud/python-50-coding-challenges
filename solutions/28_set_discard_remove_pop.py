# HackerRank - Set .discard(), .remove() & .pop()
# Topic: Sets | Difficulty: Easy

n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
print(sum(s))
