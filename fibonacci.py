#Diego Aspinwall
#10-31-17
#fibonacci.py

def fibonacci(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(3))