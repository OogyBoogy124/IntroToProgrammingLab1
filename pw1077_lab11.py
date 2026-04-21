#Parker Wood
#Lab 11

#Part 1
"""
f = open("lab11_part1.txt", "w")
print("Name of the file: ", f.name)
f.write("Python is a great language. \nYeah its great!!")

f.close()

f = open("lab11_part1.txt", "r+")
print("Name of the file: ", f.name)
str = f.read(10)
print("Read string is: ", str)

f.close()

f = open("lab11_part1.txt", "r+")
str = f.read(10)
print("Read string is: ", str)
position = f.tell() #Tells you current file position
print("Current file position: ", position)
position = f.seek(0,0); #Changes the file position
str = f.read(10)
print("Again read String is: ", str)

f.close()
"""
def rock_paper_scissors():
    f = open("C:/Users/pw1077/OneDrive - USNH/Documents/Lab 11/input.txt", "r+")
    a_wins = 0
    b_wins = 0
    num_games=int(f.readline())
    print(num_games)
    g_played=list(f.readline())
    print(g_played)
    for i in range(num_games):
        if i == 0:
            a_action = g_played[i]
            b_action = g_played[(i+1)]
        else:
            a_action = g_played[i+2]
            b_action = g_played[i+3]
        print(a_action)
        print(b_action)
        print("Game: ",i)
        if a_action == b_action:
            print("Draw")

    
    """for i in range(len(sequence) // 2):
        a_action = sequence[i]
        b_action = sequence[(i+1)]
        print(a_action)
        print(b_action)
        print("Game: ",i)
        if a_action == 'R' and b_action == "R":
            print("DRAW")
        elif a_action == "R" and b_action == "S":
            print("A WINS")
            a_wins += 1
        elif a_action == "R" and b_action == "P":
            print("B WINS")
            b_wins += 1
        elif b_action == "R" and a_action == "S":
            print("A WINS")
            a_wins += 1
        elif b_action == "R" and a_action == "P":
            print("B WINS")
            b_wins += 1
        elif a_action == "P" and b_action == "S":
            print("B WINS")
            b_wins += 1
        elif a_action == "S" and b_action == "P":
            print("A WINS")
            a_wins += 1
    if a_wins > b_wins:
        print("A WINS TOURNAMENT")
    else:
        print("B WINS TOURNAMENT")
    """
    f.close()

def main():
    #Part 2
    rock_paper_scissors()

if __name__=="__main__":
    main()
