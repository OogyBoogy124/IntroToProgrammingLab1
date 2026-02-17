#Parker Wood
#Lab 04

import math

def is_triangle(x,y,z):
    #Part 1
    if (x+y) < z:
        print("A triangle cannot have side of length ", x, ",", y, ", and ", z)
    elif (x+z) < y:
        print("A triangle cannot have side of length ", x, ",", y, ", and ", z)
    elif (y+z) < x:
        print("A triangle cannot have side of length ", x, ",", y, ", and ", z)
    else:
        print("A triangle can have side of length ", x, ",", y, ", and ", z)
        return

def print_whether_right_triangle(x,y,z):
    #is_triangle(x,y,z) #Checking if the numbers can make a triangle
    c=0
    b=0
    a=0
    if (x and y) < z:
        c = z
        b = x
        a = y
        if (a**2) + (b**2) == (c**2):
            print("A right triangle can have sides of length" , x, ",", y, ", and ", z)
        else:
            print("A right triangle cannot have sides of length" , x, ",", y, ", and ", z)
    if (x and z) < y:
        c = y
        b = x
        a = z
        if (a**2) + (b**2) == (c**2):
            print("A right triangle can have sides of length" , x, ",", y, ", and ", z)
        else:
            print("A right triangle cannot have sides of length" , x, ",", y, ", and ", z)
    if (y and z) < x:
        c = x
        b = y
        a = z
        if (a**2) + (b**2) == (c**2):
            print("A right triangle can have sides of length" , x, ",", y, ", and ", z)
        else:
            print("A right triangle cannot have sides of length" , x, ",", y, ", and ", z)
    

def check_is_square():
    #Part 3
    x1 = int(input("Please enter the coordinates for X1: "))
    y1 = int(input("Please enter the coordinates for y1: "))
    x2 = int(input("Please enter the coordinates for X2: "))
    y2 = int(input("Please enter the coordinates for Y2: "))
    x3 = int(input("Please enter the coordinates for X3: "))
    y3 = int(input("Please enter the coordinates for Y3: "))
    x4 = int(input("Please enter the coordinates for X4: "))
    y4 = int(input("Please enter the coordinates for Y4: "))

    d1 = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    d2 = math.sqrt(((x4-x3)**2)+((y4-y3)**2))
    d3 = math.sqrt(((x3-x1)**2)+((y3-y1)**2))
    d4 = math.sqrt(((x4-x2)**2)+((y4-y2)**2))

    if (d1 and d2) == (d3 and d4):
        print("Yes - it is a square")
    else:
        print("No - it is not a square")


def conversations():
    #Part 4
    s = input()
    if s == "Bye" or s == "bye":
        print("Have a nice day!")
        return
    else:
        print("Did you say ", s, "?")
        conversations()

def cascade(n):
    #Part 5
    #Divide each number by 10 using //

def main():
    #Part 1
    '''
    a = int(input("Please enter a real number for one side of the triangle: "))
    b = int(input("Please enter a real number for another side of the triangle: "))
    c = int(input("Please enter a real number for the last side of the triangle: "))'''
    #is_triangle(a,b,c)
    #Part 2
    #print_whether_right_triangle(a,b,c)
    #Part 3
    #check_is_square()
    #Part 4
    #conversations()
    n = int(input("Please enter an integer: "))
    cascade(n)
    



if __name__=='__main__':
    main()
