#Diego Aspinwall
#sunrise.py
#10-26-17

from ggame import *
def moveCircle():
    
    circle.y = circle.y - 1

if __name__ == '__main__':

    black = Color(0x000000,1)
    green = Color(0x0000FF,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (500,600))
    App().run(moveCircle)

