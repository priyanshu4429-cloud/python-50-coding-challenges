# HackerRank - Map and Lambda Function
# Topic: Functional | Difficulty: Easy

cube = lambda x: x ** 3
def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

n = int(input())
print(list(map(cube, fibonacci(n))))
