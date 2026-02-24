#Parker Wood
#Lab 05


def partial_countdown(count, step):
    #Part 1

    if count < 1: #Checking to see if the number is less than 1
        print('Blastoff!')
    elif count <= 10: #Checking to see if the number is less then 10
        print(count)
        count -= 1 #Counting down the numbers by 1
        partial_countdown(count, step)
    else:
        divisible_check = count % step 
        if divisible_check > 0: #Checking to see if the number is divisible by the step
            count -= divisible_check
            print(count)
            partial_countdown(count, step)
        else:
            count -= step
            if count <= 10: #If the count is less than 10, it will return 10 here instead of skipping over it
                print('10')
                partial_countdown(count, step)
            else:
                print(count)
                partial_countdown(count, step)
    


def print_first_n_multiples(n, num_multiples):
    #Part 2
    
    if num_multiples > 0:
        print(n, end = ' ')
        
        num_multiples -= 1
        print_first_n_multiples(n, num_multiples)
    else:
        return

def print_whether_n_looks_indivisible(n,x):
    #Part 3
    if x < 2:
        print(n, " looks like it's indivisible for the given range")
    if x >= n:
        print(n, " looks like it's indivisible for the given range")
    else:
        divisible_check = n % x
        if divisible_check == 0:
            print(n, " is divisable by ", x)
        else:
            print_whether_n_looks_indivisible(n,x-1)




def main():
    #Part 1
    #partial_countdown(20, 3)
    #Part 2
    #print_first_n_multiples(5, 3)
    print_whether_n_looks_indivisible(25,24)

if __name__=='__main__':
    main()
