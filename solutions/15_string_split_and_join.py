# HackerRank - String Split and Join
# Topic: Strings | Difficulty: Easy

def split_and_join(line):
    return '-'.join(line.split())

line = input()
print(split_and_join(line))
