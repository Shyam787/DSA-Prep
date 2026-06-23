def fibonacci(n):

    # base/terminating condition
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # recursive decomposition
    return fibonacci(n-1) + fibonacci(n-2)

n = 6
print(fibonacci(n))