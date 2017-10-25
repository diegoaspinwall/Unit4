#Diego Aspinwall
#10-25-17
#bouncingBall.py

from ggame import *
def moveCircle():
    circle.x = circle.x+1
    cicle.y = circle.y+1
    data['frames'] = 0
    
    if circle.y > 0:
        circle.y -= ?
    if circle.y < 600:
        circle.y += ?
    if circle.x > 0:
        circle.x -= ?
    if circle.x < 1000:
        circle.x += ?
    
def step():
    data['frames'] += 1
    if data['frames'] == 1:
        moveCircle()

if _name_ == '_main_':
    
    black = Color(0x000000,1)
    green = Color(0x00FF00,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    ball = Sprite(greenCircle, (50,50))
    App().run(step)
