#Diego Aspinwall
#10-23-17
#triangle.py

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))

def distance(z,d,y,q):
    return (((z-y)**2+(d-q)**2)**(1/2))

a = distance(x1,y1,x2,y2)
b = distance(x2,y2,x3,y3)
c = distance(x1,y1,x3,y3)
s = (1/2)*(a+b+c)

print('Area = ', (s*(s-a)*(s-b)*(s-c))**(1/2))