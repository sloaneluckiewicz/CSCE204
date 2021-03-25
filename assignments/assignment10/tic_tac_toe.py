# Author: Sloane Luckiewicz
# Functions with Return Values

import turtle
screen = turtle.Screen()
screen.setup(500,500)
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor("lavenderblush")
screen.tracer(0,0)
pen = turtle.Turtle()
pen.hideturtle()

def draw_grid():
    pen.pencolor("black")
    pen.pensize(5)
    pen.up()
    pen.setpos(-turtle.window_width()/100,-1)
    pen.setheading(0)
    pen.down()
    pen.forward(turtle.window_width())
    pen.up()
    pen.setpos(-turtle.window_width()/100,1)
    pen.setheading(0)
    pen.down()
    pen.forward(turtle.window_width())
    pen.up()
    pen.setpos(-1,-turtle.window_height()/100)
    pen.setheading(90)
    pen.down()
    pen.forward(turtle.window_height())
    pen.up()
    pen.setpos(1,-turtle.window_height()/100)
    pen.setheading(90)
    pen.down()
    pen.forward(turtle.window_height)

def draw_o(x,y): 
    pen.up()
    pen.goto(x,y-0.75)
    pen.setheading(0)
    pen.color("black")
    pen.down()
    pen.circle(0.75, steps=100)

def draw_x(x,y):
    pen.color("black")
    pen.up()
    pen.setpos(x-0.75,y-0.75)
    pen.down()
    pen.setpos(x+0.75,y+0.75)
    pen.up()
    pen.setpos(x-0.75,y-0.75)
    pen.down()
    pen.setpos(x+0.75,y+0.75)

def draw_piece(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==1:
        draw_x(x,y)
    else:
        draw_o(x,y)

def drawPlay(board):
    draw_grid()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,board[i][j])
    screen.update()

def gameover(board):
    if board[0][0]>0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]: return board[0][0]
    if board[1][0]>0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]: return board[1][0]
    if board[2][0]>0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]: return board[0][0]
    if board[0][1]>0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]: return board[0][1]
    if board[0][2]>0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]: return board[0][2]
    if board[0][0]>0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]: return board[0][0]
    if board[2][0]>0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]: return board[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if board[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0

def play(x,y):
    global turn
    i = 3-int(y+5)//2
    j = int(x+5)//2-1
    if i>2 or j>2 or i<0 or j<0 or board[i][j]!=0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    drawPlay(board)
    r = gameover(board)
    if r==1:
        screen.textinput("Game over!","X won!")
    elif r==2:
        screen.textinput("Game over!","O won!")
    elif r==3:
        screen.textinput("Game over!", "Tie!")

board = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
drawPlay(board)
turn = 'x'
screen.onclick(play)
turtle.mainloop()