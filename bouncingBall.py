#Diego Aspinwall
#10-25-17
#bouncingBall.py

from ggame import *

if _name_ == '_main_'

black = Color(0x000000,1)
green = Color(0x00FF00,1)

greenCircle = CircleAsset(50,LineStyle(1,green),green)
blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)

def moveCircle():
    circle.x = randint(0,COLS-1)*CELL_SIZE
    cicle.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0

Sprite(blackRectangle)
ball = Sprite(greenCircle, (50,50))
App().run()
