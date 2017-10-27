#Diego Aspinwall
#10-27-17
#bouncingBall.py

from ggame import *

X_LENGTH = 1000
Y_LENGTH = 600
CIRCLE_R = 40
PADDLE_X = 40
PADDLE_Y = 200

def moveUp(event):
    if paddle1.y > 0:
        paddle1.y -= data[p1]
def moveDown(event):
    if paddle1.y < Y_LENGTH-Y_LENGTH:
        paddle1.y += data[p1]


def moveCircle():
    
    circle.x = circle.x+data['directionx']
    circle.y = circle.y+data['directiony']
    
    if circle.y == CIRCLE_R or circle.y == Y_LENGTH-CIRCLE_R:
        data['directiony'] = -1*data['directiony']
    '''if circle.x == CIRCLE_R or circle.x == X_LENGTH-CIRCLE_R:
        data['directionx'] = -1*data['directionx']'''

if __name__ == '__main__':
    
    data = {}
    data['directionx'] = 10
    #data['directiony'] = 10
    data['p1'] = 0
    data['p2'] = 0
    
    black = Color(0x000000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    
    greenCircle = CircleAsset(CIRCLE_R,LineStyle(1,green),green)
    blackRectangle = RectangleAsset(X_LENGTH,Y_LENGTH,LineStyle(1,black),black)
    paddleBox1 = RectangleAsset(PADDLE_X,PADDLE_Y,LineStyle(1,blue), blue)
    paddleBox2 = RectangleAsset(PADDLE_X,PADDLE_Y,LineStyle(1,blue), blue)
    
    Sprite(blackRectangle)
    circle = Sprite(greenCircle, (CIRCLE_R+10,CIRCLE_R+10))
    paddle1 = Sprite(paddleBox1, ((X_LENGTH-PADDLE_X),(Y_LENGTH/2-PADDLE_Y/2)))
    paddle2 = Sprite(paddleBox1, ((0),(Y_LENGTH/2-PADDLE_Y/2)))
    
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(moveCircle)
