#Diego Aspinwall
#10-24-17
#colorChangeWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    numcolor = randint(1,4)
    if numcolor==1:
        color = Color(0xff0000, 1)
    elif numcolor==2:
        color = Color(0x0000ff, 1)
    elif numcolor==3:
        color = Color(0xffff00, 1)
    elif numcolor==4:
        color = Color(0x00ff00, 1)
    line = LineStyle(3,color)
    radius = randint(1,200)
    circle = CircleAsset(radius,line,color)
    Sprite(circle, (randint(radius,200),randint(radius,200)))
App().listenMouseEvent('click', mouseClick)
App().run()

