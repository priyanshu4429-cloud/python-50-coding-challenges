# HackerRank - Alphabet Rangoli
# Topic: Strings | Difficulty: Easy

import string

def rangoli(n):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(n):
        s = '-'.join(alpha[i:n])
        lines.append((s[::-1] + s[1:]).center(4*n-3, '-'))
    print('\n'.join(lines[::-1] + lines[1:]))

n = int(input())
rangoli(n)
