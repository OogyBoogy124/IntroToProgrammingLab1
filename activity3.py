import turtle
import time

screen = turtle.Screen() #Make a canvas to draw

screen.title("CS2370")
screen.bgcolor('black') #changing back ground color

turtle1 = turtle.Turtle()
turtle1.color('white')
turtle2 = turtle.Turtle()
turtle2.color('white')
turtle3 = turtle.Turtle()
turtle3.color('white')
turtle4 = turtle.Turtle()
turtle4.color('white')

turtle1.forward(50) #X-axis
time.sleep(2)#Seconds
turtle2.left(90)#Turns 90 degrees
turtle2.forward(90)
turtle3.right(100)
turtle3.forward(100)

turtle4.pu()#Pen up
turtle4.goto(90,100)
print(turtle4.pos())
turtle4.pd()#Pen Down
turtle4.goto(-90, -100)

turtle4.shape("turtle")
turtle3.setposition(-200, 100)
turtle3.home()
