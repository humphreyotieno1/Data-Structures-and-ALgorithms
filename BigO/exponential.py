# fibonacci series using exponential time complexity
def fibonacci(n):
    if n <= 1:
        return n
    
    branch1 = fibonacci(n -1)
    branch2 = fibonacci(n - 2)
    
    return branch1 + branch2

for i in range(10):
    print(fibonacci(i))

print(fibonacci(10))