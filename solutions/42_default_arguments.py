# HackerRank - Default Arguments
# Topic: Functions | Difficulty: Easy

def print_from_to_n(n, f=1):
    for i in range(f, n+1):
        print(i)

print_from_to_n(int(input()))
