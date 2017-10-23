#Diego Aspinwall
#10-23-17
#warmup11.py

def isPrime(n):
    for i in range(2,n+1):
        if n%i==0:
            return False
        else:
            return True

print(isPrime(7))
