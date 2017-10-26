#Diego Aspinwall
#sunrise.py
#10-26-17

from ggame import *
def moveCircle():
    circle.x = circle.x - .5
    circle.y = circle.y - 1

if __name__ == '__main__':

    black = Color(0x66B2FF,1)
    green = Color(0xFFFF66,1)
    
    greenCircle = CircleAsset(50,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(1000,600,LineStyle(1,black),black)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (500,600))
    App().run(moveCircle)

