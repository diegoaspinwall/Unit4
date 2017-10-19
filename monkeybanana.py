#Diego Aspinwall
#10-19-17
#monkeybanana.py - best game ever

from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE, LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()
