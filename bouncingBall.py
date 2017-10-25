#Diego Aspinwall
#10-25-17
#bouncingBall.py

from ggame import *

black = Color(0x000000,1)
green = Color(0x00FF00,1)

greenCircle = CircleAsset(50,LineStyle(1,green),green)
blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)

Sprite(blackRectangle)
Sprite(greenCircle, (50,50))
App().run()
