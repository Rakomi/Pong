import turtle
import os
import time
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
x = 0
s = 0
m = 8 #must be 7.5 at first
r = 1
dd = m/3
mp = 2

def update():
    pen.goto(0, 220)
    pen.write("A/Z to move Paddle 1\nUp/Down to move Paddle 2", align="center", font=("Courier", 13, "normal"))
    pen.goto(0, 260)
    pen.write("Player 1: {} Player 2: {}".format(sa, sb), align="center", font=("Courier", 24, "italic"))
    pen.goto(0, -250)
    #pen.write("Round {}".format(r), align="center", font=("Courier", 15, "bold"))
    pen.write("Round {} | M {} | DD {} | S {}".format(r, m, dd ,s), align="center", font=("Courier", 15, "bold"))

#P A
pd_a = turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.color("white")
pd_a.shapesize(stretch_wid=5, stretch_len=1)
pd_a.penup()
pd_a.goto(-350, 0)

#P B
pd_b = turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.color("white")
pd_b.shapesize(stretch_wid=5, stretch_len=1)
pd_b.penup()
pd_b.goto(350, 0)

#Ball
ba = turtle.Turtle()
ba.speed(0)
ba.shape("square")
ba.color("white")
ba.penup()
ba.goto(0, 0)
ba.dx = dd
ba.dy = dd

#Score
sa = 0
sb = 0

#Pen A
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
update()

#functions
def pause(sec):
    m = 0
    time.sleep(sec)

def pdau():
    y = pd_a.ycor()
    y += 20
    pd_a.sety(y)

def pdad():
    y = pd_a.ycor()
    y -= 20
    pd_a.sety(y)

def pdbu():
    y = pd_b.ycor()
    y += 20
    pd_b.sety(y)

def pdbd():
    y = pd_b.ycor()
    y -= 20
    pd_b.sety(y)

#binding
wn.listen()
wn.onkeypress(pdau, "a")
wn.onkeypress(pdad, "z")
wn.onkeypress(pdbu, "Up")
wn.onkeypress(pdbd, "Down")

#Main game loop and border checking
while True:
    wn.update()
    ba.setx(ba.xcor() + ba.dx)
    ba.sety(ba.ycor() + ba.dy)

    if ba.ycor() > 290:
        ba.sety(290)
        ba.dy *= -1
        os.system("afplay bounce.wav&")

    if ba.ycor() < -290:
        ba.sety(-290)
        ba.dy *= -1
        os.system("afplay bounce.wav&")

    if ba.xcor() > 390:
        ba.goto(0, 0)
        ba.dx *= -1
        sa += 1
        m += mp
        pen.goto(0, 260)
        pen.clear()
        update()
        os.system("afplay score.wav&")
        ba.dx = dd
        ba.dy = dd
        dd = m / 4

    if ba.xcor() < -390:
        ba.goto(0, 0)
        ba.dx *= -1
        sb += 1
        m += mp
        pen.goto(0, 260)
        pen.clear()
        update()
        os.system("afplay score.wav&")
        ba.dx = dd
        ba.dy = dd
        dd = m / 4

    #paddle interaction b
    if ba.xcor() > 340 and ba.xcor() < 350 and (ba.ycor() < pd_b.ycor() + 60 and ba.ycor() > pd_b.ycor() -60):
        ba.setx(340)
        ba.dx *= -1
        os.system("afplay hit.wav&")

    # paddle interaction b
    if ba.xcor() < -340 and ba.xcor() > -350 and (ba.ycor() < pd_a.ycor() + 60 and ba.ycor() > pd_a.ycor() -60):
        ba.setx(-340)
        ba.dx *= -1
        os.system("afplay hit.wav&")
