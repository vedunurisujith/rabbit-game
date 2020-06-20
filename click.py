import turtle
import time
import random


delay=0.05
wn = turtle.Screen()
wn.title("mygame")
wn.bgcolor("black")
wn.bgpic("img.gif")
wn.setup(width=800,height=600)
wn.tracer(0)
wn.register_shape("rabbit.gif")
wn.register_shape("raj.gif")
wn.register_shape("carat.gif")
wn.register_shape("im.gif")
wn.register_shape("der.gif")
score =0
power=0
total=0
#pen
pen=turtle.Turtle()
pen.hideturtle()
pen.shape("square")
pen.color("red")
pen.penup()
pen.goto(0,250)
pen.write("score :{} power : {} total :{}".format(score,power,total),align="center",font=("carrirer",24,"normal"))


good = []
bad=[]
#player
p=turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.shapesize(stretch_wid=4,stretch_len=4)
p.penup()
p.shape("rabbit.gif")
p.goto(0,-260)
p.direction="stop"

#good players
for i in range(10):
    g=turtle.Turtle()
    g.speed(0)
    g.shape("circle")
    g.color("red")
    g.shapesize(stretch_wid=4,stretch_len=4)
    g.shape("carat.gif")
    g.penup()
    g.goto(random.randint(-380,380),280)
    good.append(g)

#bad players
for i in range(5):
    b=turtle.Turtle()
    b.speed(0)
    b.shape("circle")
    b.color("red")
    b.shapesize(stretch_wid=2,stretch_len=2)
    b.penup()
    b.goto(random.randint(-380,380),280)
    bad.append(b)

#moving function
def pleft():
    p.direction="left"
def pright():
    p.direction="right"
    
#moving players from the keyboard
wn.listen()
wn.onkeypress(pleft,"Left")
wn.onkeypress(pright,"Right")

#main method
while True:
    wn.update()
    time.sleep(delay)

    if p.direction=="right":
        p.shape("rabbit.gif")
        p.setx(p.xcor() +10)
    if p.direction=="left":
        p.shape("raj.gif")
        p.setx(p.xcor() -10)

    #off the screen player
    if p.xcor() >390:
        p.setx(-380)
        
    if p.xcor() <-390:
        p.setx(380)
    for g in good:
        y=g.ycor()
        y -=5
        g.sety(y)
        #off the screen
        if g.ycor()<-290:
            g.goto(random.randint(-380,380),280)


        #collision
        if g.distance(p)<60:
            pen.clear()
            score +=20
            total=score+power
            pen.write("score :{} power : {} total :{}".format(score,power,total),align="center",font=("carrirer",24,"normal"))
            g.goto(random.randint(-380,380),280)
    for b in bad:
        y=b.ycor()
        y -=5
        b.sety(y)
        #off the screen
        if b.ycor()<-290:
            b.goto(random.randint(-380,380),280)


        #collision
        if b.distance(p)<60:
            pen.clear()
            power -=20
            total=score+power
            pen.write("score :{} power : {} total :{}".format(score,power,total),align="center",font=("carrirer",24,"normal"))
            b.goto(random.randint(-380,380),280)
