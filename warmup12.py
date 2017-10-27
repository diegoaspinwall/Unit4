#Diego Aspinwall
#10-27-17
#warmup12.py

def GCF(num1,num2):
    if num1>num2:
        for i in range(num1,1):
            if num2%i==0:
                return i
    else:
        for i in range(num2,1):
            if num2%i==0:
                return i

print(GCF(10,5))