#Diego Aspinwall
#10-25-17
#bouncingBall.py

from ggame import *
def moveCircle():
    
    circle.x = circle.x+data['directionx']
    circle.y = circle.y+data['directiony']
    
    if circle.y == 50:
        data['directiony'] = -1*data['directiony']
    if circle.y == 550:
        circle.y = circle.y + 1
    if circle.x == 50:
        circle.x = circle.x - 1
    if circle.x == 950:
        circle.x = circle.x + 1
    
def step():
    moveCircle()

if __name__ == '__main__':
    
    data = {}
    data['directionx'] = 1
    data['directiony'] = 1
    
    black = Color(0x000000,1)
    green = Color(0x00FF00,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (50,50))
    App().run(step)
