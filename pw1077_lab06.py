#Parker Wood
#Lab 06


def GCD(x,y):
    #Part 1
    while y > 0: #Exit the loop if the remainder is 0
        r = x%y #Making the remainder
        x = y #Reseting numbers
        y = r
    print(x, "Is the GCD")

def ReverseDigits(n):
    #Part 2
    new_list = 0
    while n>0:
        remainder = n%10 #Grabs the number from the end of the list
        n = n//10 #Gets rid of that ending number
        new_list = (new_list*10) + remainder #Adds that number to the new list from the beginning
        
    print(new_list, "is the new reversed number")

#def Fibonacci(n):
    #Part 3
    
def Factoral(n):
    #Part 4
    x = n
    while x>0:
        
        
    print(x, "is the answer")



    
def main():
    #Part 1
    #GCD(20,12)
    #Part 2
    #ReverseDigits(12345)
    #Part 3
    #Part 4
    Factoral(5)


main()
