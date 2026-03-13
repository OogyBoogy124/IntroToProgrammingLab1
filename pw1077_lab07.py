#Parker Wood
#Lab 07


def p_square(rows):
    #Part 1
    for i in range(rows):#i = 0,1,2,...rows
        print((chr(65+i) + ' ') * rows) #Creating the character and adding it with i
        

def LTriangle(row):
    #Part 2
    x = row*2 #Setting the amount of spaces needed to fit all of the letters in the triangle
    for i in range(row): #i = 0,1,2,...row
        print(" "*x, ((chr(65+i) + ' ') * (i+1))) 
        x = x-2 #Removes spaces to make the letters line up properly

def reverse_triangle(n): #n = num of rows
    #Part 3
    x=n+1 #Setting a variable to help count the letters
    for i in range(n):
        print(" " * i, end='') #Making spaces after each set of letters
        for p in range(1, x-i): #This loop is used to print an accurate amount of letters for each set
            print(chr(64+p), end="")
        print()
        
def side_ways_arrow(n): #n = the starting number
    #Part 4
    #Loop for counting up
    for i in range(n+1): #Loop to repeat the inner loop properly
        for p in range(0, 1+i): #Loop to print out the numbers in the line each time 
            print(n-p, end=' ') #
        print()
    
    x = n + 1
    #Loop for counting down
    for i in range(n+1):
        for p in range(1, (n+1)-i):#Loop for printing each number that is meant to be in the line
            print(x-p, end=' ')
        print()


def Triangle(row):
    #Part 5
    x=row
    for i in range(row+1):
        print(" " * i, end='') 
        for p in range(0, x-i): 
            print((row-i)-p, "", end="")
        print()

def mirror_num_diamond(n): #n = what number we're counting up to
    #Part 6
    for i in range(n+1):
        print(" " * (n-i), end='')
        for p in range(1, i+1):
            print(p, "", end="")
        print()
    for i in range(n+1):
        print(" " * (i+1), end='')
        for p in range(1, n-i):
            print(p, "", end="")
        print()

def diamond(n):
    #Part 7
    for i in range(n+1):
        print(" " * (n-i), end='')
        for p in range(0, n-1):
            if p == 0:
                print("*")
            else:
                print("*", " " * (p+1), "*")
    
def star_arrow(n):
    #Part 8
    x = n/2
    y = x/2
    for i in range(1, int(x+1)):
        print(" "*(int(x-i)), "*"*(i-1))
    

def main():
    #Part 1
    """a = int(input("Enter number of rows: "))
    p_square(a)
    #Part 2
    b = int(input("Enter number of rows: "))
    LTriangle(b)
    #Part 3
    c = int(input("Enter number of rows: "))
    reverse_triangle(c)
    #Part 4
    d = int(input("Enter number of rows: "))
    side_ways_arrow(d)
    #Part 5
    e = int(input("Enter number of rows: "))
    Triangle(e)
    #Part 6
    f = int(input("Enter number of rows: "))
    mirror_num_diamond(f)"""
    #Part 7
    #g = int(input("Enter number of rows: "))
    #diamond(g)
    #Part 8
    h = int(input("Enter number of rows: "))
    star_arrow(h)

if __name__ == "__main__":
    main()
