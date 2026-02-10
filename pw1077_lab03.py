#Parker Wood
#Lab 3
import turtle
from turtle import *
import math

bob = turtle.Turtle()


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def SetTurtle(t, x, y, angle):
    t.pu()
    t.lt(angle)
    t.goto(x,y)
    t.pd()

def house(t):
    for i in range(2): #Making the base of the house
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
        
    t.forward(90)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)#Making the door
    t.right(90)
    t.forward(40)
    t.left(90)
    
    t.forward(90)
    t.left(90)
    t.forward(100)
    t.left(60)
    t.forward(115)#Making the roof
    t.left(60)
    t.forward(115)
    
#square(bob, 250)
#polygon(bob, 30, 8)
#circle(bob, 10)
#arc(bob, 40, 270)

house(bob)

turtle.mainloop()
