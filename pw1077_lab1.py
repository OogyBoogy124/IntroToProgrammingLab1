def print_checker_boundary_row():
    print("+-+-+-+-+-+-+-+-+")
def print_checker_space_row():
    #Part 12
    print("| | | | | | | | |") 

def loop_print_checker():
    #Part 13
    print_checker_boundary_row()
    print_checker_space_row()

def print_checker_spaces_under_boundary():
    #part 14
    print("+-+-+-+-+-+-+-+-+")
    print("| | | | | | | | |")

def print_draughts_space_row():
    #Part 20
    print("| | | | | | | | | | |")

def print_draughts_boundary_row():
    #Part 21
    print("+-+-+-+-+-+-+-+-+-+-+")

def print_draughts_spaces_under_boundary():
    #Part 21
    print_draughts_space_row()
    print_draughts_boundary_row()

def draw_draughts_board():
    #Part 22
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_spaces_under_boundary()
    print_draughts_boundary_row()

def draw_checker_board():
    #Part 23
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_boundary_row()


def space_row_with_checkers_circle():
    print("| |O| |O| |O| |O|")

def space_row_with_checkers_xs():
    print("| |X| |X| |X| |X|")

def draw_checker_board_with_pieces():
    
    
def main():
    print('Running tests...')
    print()
    #Part 17
    print('Output for print_checker_boundary_row():')
    print_checker_boundary_row()
    print()
    #part 17
    print('Output for print_checker_space_row():')
    print_checker_space_row()
    print()
    #Part13
    """for i in range(0,8):
        #Part 13
        loop_print_checker()"""


    print('Now print the entire checker board')
    #Part 14
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_spaces_under_boundary()
    print_checker_boundary_row()

#Part 16
if __name__ == '__main__':
    main()
