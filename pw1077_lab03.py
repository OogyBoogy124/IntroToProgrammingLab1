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
    t.forward(116)#Making the roof
    t.left(60)
    t.forward(116)

    t.left(90)
    t.pu()
    t.forward(50)
    t.pd()
    circle(bob,20)#Making Window 1
    
    t.left(60)
    t.pu()
    t.forward(120)
    t.right(90)
    t.forward(12)
    t.left(90)
    t.pd()
    circle(bob, 20)#Making Window 2

def olympic_rings(t):
    t.color('blue')#Top ring 1
    circle(t, 40)
    t.pu()
    t.forward(60)
    t.pd()
    t.color('green') #Top ring 2
    circle(t, 40)
    t.pu()
    t.forward(60)
    t.pd()
    t.color('red') #Top ring 3
    circle(t, 40)
    t.pu()
    t.goto(0, 0)#Reseting position for bottom rings
    t.right(90)
    t.forward(50)#Moving down
    t.left(90)
    t.forward(30)
    t.pd()
    t.color('brown') #Bottom ring 1
    circle(t, 40)
    t.pu()
    t.forward(60)
    t.pd()
    t.color('yellow') #Bottom ring 2
    circle(t, 40)

def cube(t):
    for i in range(2): #Making first rectangle
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.left(90)
    t.forward(50)
    t.left(135)
    t.forward(50)#Making the first 3D line
    t.left(45)
    t.forward(50)
    t.left(90)
    for i in range(2): #Making second rectangle
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.goto(0, 0)
    t.goto(100,0)#Attaching the rest of the 3D lines
    t.right(135)
    t.forward(50)
    t.right(135)
    t.forward(50)
    t.goto(100,50)
    
#square(bob, 250)
#polygon(bob, 30, 8)
#circle(bob, 10)
#arc(bob, 40, 270)
#house(bob)
#olympic_rings(bob)
cube(bob)

turtle.mainloop()
