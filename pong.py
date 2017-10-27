#Diego Aspinwall
#10-27-17
#bouncingBall.py

from ggame import *

X_LENGTH = 1000
Y_LENGTH = 600

def moveCircle():
    
    circle.x = circle.x+data['directionx']
    circle.y = circle.y+data['directiony']
    
    if circle.y == 50 or circle.y == Y_LENGTH-50:
        data['directiony'] = -1*data['directiony']
    if circle.x == 50 or circle.x == X_LENGTH-50:
        data['directionx'] = -1*data['directionx']

if __name__ == '__main__':
    
    data = {}
    data['directionx'] = 10
    data['directiony'] = 10
    
    black = Color(0x000000,1)
    green = Color(0x0000FF,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(X_LENGTH,Y_LENGTH,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (50,50))
    App().run(moveCircle)
