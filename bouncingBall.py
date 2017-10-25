#Diego Aspinwall
#10-25-17
#bouncingBall.py

from ggame import *
def moveCircle():
    
    circle.x = circle.x+data['directionx']
    circle.y = circle.y+data['directiony']
    
    if circle.y == 50 or circle.y == 550:
        data['directiony'] = -1*data['directiony']
    if circle.x == 50 or circle.x == 950:
        data['directionx'] = -1*data['directionx']

if __name__ == '__main__':
    
    data = {}
    data['directionx'] = 10
    data['directiony'] = 10
    
    black = Color(0x000000,1)
    green = Color(0x0000FF,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (50,50))
    App().run(moveCircle)
