#Diego Aspinwall
#10-20-17
#printSquares.py

def printSquares(x,y):
    for j in range(0,y):
        for i in range(0,1):
            print('+ -- '*x, '+')
            print('|    '*x, '|')
    print('+ -- '*x, '+')
printSquares(2,3)