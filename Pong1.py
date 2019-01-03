# pong in python 3 for beginners - from tutorial by @TokyoEdTech
# i left out the sound files
# importing turtle module
import turtle
# setting up a window
wn = turtle.Screen()
wn.title('Pong Tutorial')
wn.bgcolor('black')
wn.setup(width = 800, height = 600)
#tracer - stops window from updating, so we can alter update rate later?
wn.tracer(0)

# score vars
score_a = 0
score_b = 0
# paddle A
paddle_a = turtle.Turtle()
#set paddle animation speed to maximum
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('green')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#removes the turtle tracing line
paddle_a.penup()
#places the paddle
paddle_a.goto(-350,0)

def make_paddle(paddle_new,width,length,posX,posY):
    paddle_new.speed(0)
    paddle_new.shape('square')
    paddle_new.color('green')
    paddle_new.shapesize(stretch_wid=width, stretch_len=length)
    paddle_new.penup()
    paddle_new.goto(posX,posY)
    return
# paddle B - instead of copying and pasting as per the tutorial
# I make a more general function to create all the paddles I want
paddle_b = turtle.Turtle()
make_paddle(paddle_b,5,1,350,0)
# Ball
#We'll do the same thing with Ball, making an even more general function
def make_object(obj_new,width,length,posX,posY,shape,color,speed):
    obj_new.speed(0)
    obj_new.shape(shape)
    obj_new.color(color)
    obj_new.shapesize(stretch_wid=width, stretch_len=length)
    obj_new.penup()
    obj_new.goto(posX,posY)
    obj_new.dx = speed
    obj_new.dy = speed
    return
ball = turtle.Turtle()
make_object(ball,1,1,0,0,'circle','white',.5)

#making a pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player_A:0   Player_B:0', align='center', font=('Courier',20,'normal'))

# functions for moving paddles
    #turtle can return coordinates with xcor,ycor
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    return
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    return
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    return
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    return

#keybinding
wn.listen()
wn.onkeypress(paddle_a_up,'w' or 'W')
wn.onkeypress(paddle_a_down, 's' or 'S')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down, 'Down')
# trying a generalized collision function
#S = paddle_b.shapesize()  #returns a triple (stretch width, stretch length,outline)
# position returns a 2d vector, (Xpos, Ypos)
# we can check the size of an object, check its position, and check for a collision
# so far, 350 and 50 represent the width and height of the object in pixels
# in fact, we're currently checking a collision between a line 350 pixels from the edge of the screen in X
# and the object in Y
def collision (game_obj_1, game_obj_2,x_col_size_1,x_col_size_2,y_col_size):
    x1 = game_obj_1.xcor()
    y1 = game_obj_1.ycor()
    x2 = game_obj_2.xcor()
    y2 = game_obj_2.ycor()
    s1 = game_obj_1.shapesize()
    s2 = game_obj_2.shapesize()
    if (x1 > (x_col_size_1) and x1 <  x_col_size_2) and  (y1 < y2 +(y_col_size) and y1 > y2 -(y_col_size) and x_col_size_1 > 0):
        return True
    if (x1 < (x_col_size_1) and x1 > x_col_size_2) and  (y1 < y2 +(y_col_size) and y1 > y2 -(y_col_size) and x_col_size_1 < 0):
        return True
#game loop
while True:
    wn.update()
    # get the ball moving
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # checking borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player_A:{}   Player_B: {}'.format(score_a,score_b), align='center', font=('Courier',20,'normal'))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player_A:{}   Player_B: {}'.format(score_a,score_b), align='center', font=('Courier',20,'normal'))

    #making collisions
        #okay the tutorial asks for a giant if statement, lets make a collision function returning a boolean
    #if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor()+40 and
    #ball.ycor() > paddle_b.ycor()-40):
    right_paddle_x_col_size = 340
    right_paddle_x_col_size_2 = 350
    paddle_y_col_size = 40
    if collision(ball,paddle_b,right_paddle_x_col_size,right_paddle_x_col_size_2,paddle_y_col_size) == True:
        ball.setx(right_paddle_x_col_size)
        ball.dx *= -1
    left_paddle_x_col_size = -340
    left_paddle_x_col_size_2 = -350
    paddle_y_col_size = 40
    if collision(ball,paddle_a,left_paddle_x_col_size,left_paddle_x_col_size_2,paddle_y_col_size) == True:
        ball.setx(left_paddle_x_col_size)
        ball.dx *= -1












    
    
