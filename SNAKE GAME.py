#Snake Game
import turtle
import random

#var
fx=0
fy=0
ft=0
size=0
score=0
highscore=0
#bg
turtle.bgcolor('cyan')

#play button

def home():
    turtle.clear()
    turtle.hideturtle()
    turtle.goto(0,0)
    turtle.write('Play',font=('Comic Sans MS',20,'italic'), align='center')# writing on screen
    turtle.onscreenclick(start)#click on screen start...
#bg
def start(x,y):
    global score, size, fx, fy, ft
    
    turtle.clear()
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pensize(20)
    turtle.pu()
    turtle.goto(-220,220)
    turtle.pd()
    turtle.color('red')
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.goto(220,220)#box outline 
    turtle.goto(220,-220)#box
    turtle.goto(-220,-220)#box
    turtle.goto(-220,220)#box
    turtle.end_fill()
    turtle.pu()
    turtle.goto(-60,240)
    turtle.write('Snake Game',font=('algerian',20,'italic'),align='center')

    turtle.end_fill()
    turtle.pu()
    turtle.goto(0,0)
    
    tfood=turtle.Turtle()
    tfood.shape('circle')
    tfood.color('red')

    tscore=turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.goto(150,-270)
    tscore.write('Score = '+str (score) ,font=('algerian',20,'italic'),align='center')

    while x>-210 and x<210 and y>-210 and y<210:
        if ft==0:
            food(tfood)
            ft=1
        x=turtle.xcor()
        y=turtle.ycor()
        move()
        turtle.listen()
        turtle.onkey(up,"Up")
        turtle.onkey(down,"Down")
        turtle.onkey(left,"Left")
        turtle.onkey(right,"Right")

        if x>fx-15 and x<fx+15 and y>fy-15 and y<fy+15:
            score+=1
            tscore.clear()
            tscore.write('Score= '+str(score),font=('algerian',20,'italic'),align='center') 
            ft=0
    tfood.hideturtle()
    tscore.clear()
    turtle.clear()
    gameover()
            
def up():
    turtle.setheading(90)

def down():
    turtle.setheading(270)

def left():
    turtle.setheading(180)

def right():
    turtle.setheading(0)
    

def move():
    global score, size
    turtle.shape('square')
    turtle.color('black')
    turtle.speed(0)
    turtle.stamp()
    turtle.fd(7) # speed of snake
    if size>score:
        turtle.clearstamps(1)
    else:
        size+=1

def food(tfood):
    global fx, fy
    fx=random.randrange(-160,160,10)
    fy=random.randrange(-160,160,10)
    tfood.pu()
    tfood.goto(fx,fy)

def gameover():
    turtle.goto(-30,20)
    turtle.color("red")
    turtle.write('Game Over',font=('algerian',50,'italic'),align='center')
    turtle.color('orange')
    turtle.goto(-10,-40)
    turtle.write('Score= '+str(score),font=('algerian',50,'italic'),align='center')
    global highscore
    if score >= highscore:
        highscore = score
        turtle.wait(5)
        turtle.write('High Score= '+str(highscore),font=('algerian',50,'italic'))


home()
import turtle

turtle.bgcolor('cyan')
turtle.write('Play',font=('Comic Sans MS',20,'italic'), align='center')# writing on screen


