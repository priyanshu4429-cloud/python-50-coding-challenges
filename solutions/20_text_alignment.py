# HackerRank - Text Alignment
# Topic: Strings | Difficulty: Easy

thickness = int(input())
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1+i) + c + (c*i).ljust(thickness-1+i))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))
for i in range(thickness):
    j = thickness-i
    print((c*j).rjust(thickness+j) + c + (c*j).ljust(thickness+j))
