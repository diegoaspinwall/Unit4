#Diego Aspinwall
#10-27-17
#bouncingBall.py

from ggame import *

X_LENGTH = 1000
Y_LENGTH = 600
CIRCLE_R = 30
PADDLE_X = 40
PADDLE_Y = 200

def moveUp(event):
    if paddle1.y > 0:
        paddle1.y -= 40
def moveDown(event):
    if paddle1.y < Y_LENGTH-PADDLE_Y:
        paddle1.y += 40
def moveUp2(event):
    if paddle2.y > 0:
        paddle2.y -= 40
def moveDown2(event):
    if paddle2.y < Y_LENGTH-PADDLE_Y:
        paddle2.y += 40


def moveCircle():
    
    circle.x = circle.x+data['directionx']
    circle.y = circle.y+data['directiony']
    
    if circle.y == CIRCLE_R or circle.y == Y_LENGTH-CIRCLE_R:
        data['directiony'] = -1*data['directiony']
    if circle.x==CIRCLE_R+PADDLE_X and paddle2.y<circle.y<paddle2.y+PADDLE_Y:
        data['directionx'] = -1*data['directionx']
    if circle.x == CIRCLE_R:
        circle.x = CIRCLE_R+PADDLE_X+10
        circle.y = CIRCLE_R+10
        data['directionx'] = 10
        data['directiony'] = 10
        updateScore2()
    if circle.x==X_LENGTH-(CIRCLE_R+PADDLE_X) and paddle1.y<circle.y<paddle1.y+PADDLE_Y:
        data['directionx'] = -1*data['directionx']
    if circle.x == (X_LENGTH-CIRCLE_R):
        circle.x = CIRCLE_R+PADDLE_X+10
        circle.y = CIRCLE_R+10
        data['directionx'] = 10
        data['directiony'] = 10
        updateScore1()

def updateScore1():
    data['score1'] += 1
    data['scoreText'].destroy()
    scoreBox = TextAsset((str(data['score1'])+'|'+str(data['score2'])),fill=scorecolor, style='bold 30pt Times')
    data['scoreText'] = Sprite(scoreBox)
    if data['score1']==10:
        print('Player 1 wins')
        data['directionx'] = 0
        data['directiony'] = 0

def updateScore2():
    data['score2'] += 1
    data['scoreText'].destroy()
    scoreBox = TextAsset((str(data['score1'])+'|'+str(data['score2'])),fill=scorecolor, style='bold 30pt Times')
    data['scoreText'] = Sprite(scoreBox)
    if data['score2']==10:
        print('Player 2 wins')
        data['directionx'] = 0
        data['directiony'] = 0


if __name__ == '__main__':
    
    data = {}
    data['directionx'] = 10
    data['directiony'] = 10
    data['score1'] = 0
    data['score2'] = 0
    
    black = Color(0x000000,1)
    circcolor = Color(0xffffff,1)
    padcolor = Color(0xffffff,1)
    scorecolor = Color(0xffffff,1)
    
    colorCircle = CircleAsset(CIRCLE_R,LineStyle(1,circcolor),circcolor)
    blackRectangle = RectangleAsset(X_LENGTH,Y_LENGTH,LineStyle(1,black),black)
    paddleBox = RectangleAsset(PADDLE_X,PADDLE_Y,LineStyle(1,padcolor), padcolor)
    scoreBox = TextAsset('0 | 0', fill=scorecolor, style='bold 30pt Times')
    
    Sprite(blackRectangle)
    circle = Sprite(colorCircle, (CIRCLE_R+PADDLE_X+10,CIRCLE_R+10))
    paddle1 = Sprite(paddleBox, ((X_LENGTH-PADDLE_X),(Y_LENGTH/2-PADDLE_Y/2)))
    paddle2 = Sprite(paddleBox, ((0),(Y_LENGTH/2-PADDLE_Y/2)))
    data['scoreText'] = Sprite(scoreBox)
    
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','w',moveUp2)
    App().listenKeyEvent('keydown','s',moveDown2)
    App().run(moveCircle)
