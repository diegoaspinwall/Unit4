#Diego Aspinwall
#10-16-17
#colorChangeWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    numcolor = randint(1,4)
    if numcolor==1:
        red = Color(0xff0000, 1)
        line = LineStyle(3,red)
        rectangle = RectangleAsset(1000,1000,line,red)
    elif numcolor==2:
        blue = Color(0x0000ff, 1)
        line = LineStyle(3,blue)
        rectangle = RectangleAsset(1000,1000,line,blue)
    elif numcolor==3:
        yellow = Color(0xffff00, 1)
        line = LineStyle(3,yellow)
        rectangle = RectangleAsset(1000,1000,line,yellow)
    elif numcolor==4:
        green = Color(0x00ff00, 1)
        line = LineStyle(3,green)
        rectangle = RectangleAsset(1000,1000,line,green)
    Sprite(rectangle)
App().listenMouseEvent('click', mouseClick)
App().run()
