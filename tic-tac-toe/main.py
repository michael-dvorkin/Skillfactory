######################################################################################
# Tic-tac-toe program
# Written by Michael Dvorkin
# 20/04/2023
#
# Description:
#
# 1. The program creates 3x3 matrix and fills it with zeros
# 2. Computer's move adds 1 to the cell
# 3. Human's move adds -1 to the cell
# 4. Computer is using the following algorythm:
#
#    a) Search for winning combination (sum of 3 horizontal, vertical
#       or diagonal cells must be 2)
#    b) If winning combination is found - win the game
#    c) Otherwise - search for other user's winning combination (sum of 3 horizontal,
#       vertical or diagonal cells must be -2)
#    d) In this case - move to cancel this combination
#    e) Check if you can create a trap - move that creates 2 winning combinations
#    f) If no trap can be created - choose cell in the following order:
#       - middle cell
#       - diagonal cell
#    g) Choose any cell that creates a possible win position
#    h) Choose any empty cell
#
# 5. At each iteration - check if the game is over (sum of 3 horizontal, vertical
#    or diagonal cells is 3 or -3) or there are no more empty cells
# 6. The game has 2 complexity levels:
#
#   0 - beginners (you can win)
#   1 - advanced (no chance)
#
# For beginners' level e, f and h are not used
######################################################################################
import random

# Matrix dimension
LEN = 3

# Gamer signs (they will be randomly changed at the beginning of the game)
MY_SIGN = 'X'
YOUR_SIGN = 'O'

# Complexity level
LEVEL = 0

def init_game():
    '''
    This function is called at the beginning of the game
    It creates empty matrix (filled by 0's)
    '''
    global MY_SIGN
    global YOUR_SIGN
    global LEVEL

    # Choose game complexity level
    # 0 - beginners (you can win)
    # 1 - advanced (no chance)
    ok = False
    while not ok:
        print('Choose complexity level: ')
        print('   0 - beginners (you can win)')
        print('   1 - advanced (no chance)')
        print('   2 - exit the game')
        answer = input('> ')
        if answer.isnumeric():
            res = int(answer)
            if res == 0 or res == 1:
                LEVEL = res
                ok = True
            elif res == 2:
                return None
            else:
                print('Choose 0, 1 or 2')
        else:
            print('Invalid choice')

    # Use pseudo-random number generator to decide who is starting the game (X is starting)
    random.seed
    res = random.random()
    if res > 0.5:
        MY_SIGN = 'O'
        YOUR_SIGN = 'X'

    print(f'You are {YOUR_SIGN}')

    # Generate empty 3x3 matrix (filled by zeros)
    M = [[0 for j in range(LEN)] for i in range(LEN)]

    return M

def print_horizontal_line():
    for j in range((LEN+1)*6+1):
        print('-', end='')
    print('')

def print_first_line():
    print('|     |', end='')
    for j in range(LEN):
        print('{:3}'.format(j), ' |', end='')
    print('')

def matrix_decorator (func):
    def wrapper(*args, **kwargs):

        print_horizontal_line()
        print_first_line()
        print_horizontal_line()

        func(*args, **kwargs)

        print_horizontal_line()

    return wrapper

@matrix_decorator
def print_matrix(M):
    '''
    This function displays matrix by replacing 1 with computer's sign,
    0 by space and -1 by gamer's sign
    '''
    global MY_SIGN
    global YOUR_SIGN

    # Print Matrix
    for i in range(LEN):
        print('|  {:1}  |'.format(i), end='')

        for j in range(LEN):
            val = ' '
            if M[i][j] == 0:
                val = ' '
            elif M[i][j] == 1:
                val = MY_SIGN
            else:
                val = YOUR_SIGN

            print('  {:1}  |'.format(val), end='')

        print("")

def your_turn(M):
    '''
    This function proposes gamer to perform his move
    '''
    print('Your move!')
    ok = False

    # Loop until user's answers are not valid
    while not ok:
        # Take vertical coordinate and check its validity
        errors = 1
        while errors > 0:
            errors = 0
            answer = input('Enter vertical coordinate (9 to exit the game): ')
            if not answer.isnumeric():
                print('Coordinate should be integer')
                errors += 1
            elif int(answer) == 9:
                return None
            elif not 0 <= int(answer) < LEN:
                print(f'Coordinate should be between 0 and {LEN-1}')
                errors += 1
        i = int(answer)

        # Take horizontal coordinate and check its validity
        errors = 1
        while errors > 0:
            errors = 0
            answer = input('Enter horizontal coordinate (9 to exit the game): ')
            if not answer.isnumeric():
                print('Coordinate should be integer')
                errors += 1
            elif int(answer) == 9:
                return None
            elif not 0 <= int(answer) < LEN:
                print(f'Coordinate should be between 0 and {LEN-1}')
                errors += 1
        j = int(answer)

        # Check that the chosen cell is free
        if M[i][j] != 0:
            print('This cell is busy, Try again')
        else:
            ok = True

    # Save the move
    M[i][j] = -1
    return M

def my_turn(M):
    '''
    This function implements win-win algorythm
    '''
    global LEVEL

    # First iteration - search for my winning combinations
    # Second iteration - search for user's winning combinations
    for d in [1, -1]:
        # Check horizontals
        for i in range(LEN):
            s = 0
            for j in range(LEN):
                s = s + M[i][j]
            # If winning combination found - do the move
            if s * d == 2:
                for j in range(LEN):
                    if M[i][j] == 0:
                        M[i][j] = 1
                return M

        # Check verticals
        for j in range(LEN):
            s = 0
            for i in range(LEN):
                s = s + M[i][j]
            # If winning combination found - do the move
            if s * d == 2:
                for i in range(LEN):
                    if M[i][j] == 0:
                        M[i][j] = 1
                return M

        # Check first diagonal
        s = 0
        for i in range(LEN):
            for j in range(LEN):
                if i == j:
                    s = s + M[i][j]
        # If winning combination found - do the move
        if s * d == 2:
            for i in range(LEN):
                for j in range(LEN):
                    if i == j:
                        if M[i][j] == 0:
                            M[i][j] = 1
            return M

        # Check second diagonal
        s = 0
        for i in range(LEN):
            for j in range(LEN):
                if i + j == LEN - 1:
                    s = s + M[i][j]
        # If winning combination found - do the move
        if s * d == 2:
            for i in range(LEN):
                for j in range(LEN):
                    if i + j == LEN - 1:
                        if M[i][j] == 0:
                            M[i][j] = 1
            return M

    # No winning combinations found

    # Check if middle cell is free (advanced level only)
    if LEVEL == 1:
        if M[1][1] == 0:
            M[1][1] = 1
            return M

    # Check if there is free corner that creates a trap - advanced level only
    if LEVEL == 1:
        for i in range(LEN):
            for j in range(LEN):
                if i%2 == 0 and j%2 == 0:
                    if M[i][j] == 0:
                        M[i][j] = 1
                        # If this move creates a trap - use it!
                        if trap_position(M, 2):
                            return M
                        else:
                            M[i][j] = 0

    # Check if there is any free corner - advanced level only
    if LEVEL == 1:
        for i in range(LEN):
            for j in range(LEN):
                if i%2 == 0 and j%2 == 0:
                    if M[i][j] == 0:
                        M[i][j] = 1
                        return M

    # Any move that creates a winning combination
    for i in range(LEN):
        for j in range(LEN):
            if M[i][j] == 0:
                M[i][j] = 1
                # If this move creates possible winning combination - use it!
                if trap_position(M, 1):
                    return M
                else:
                    M[i][j] = 0

    # Any move is fine...
    for i in range(LEN):
        for j in range(LEN):
            if M[i][j] == 0:
                M[i][j] = 1
                return M

    # No free cells
    return M

def trap_position(M, lvl):
    '''
    This function searches for traps
    If there are 2 and more winning positions - the trap exists
    If there is 1 winning position - there is a possible winning combination
    '''
    pos = 0

    # Check horizontals for winning positions
    for i in range(LEN):
        s = 0
        for j in range(LEN):
            s = s + M[i][j]
        if s == 2:
            pos = pos + 1

    # Check verticals for winning positions
    for j in range(LEN):
        s = 0
        for i in range(LEN):
            s = s + M[i][j]
        if s == 2:
            pos = pos + 1

    # Check first diagonal for winning positions
    s = 0
    for i in range(LEN):
        for j in range(LEN):
            if i == j:
                s = s + M[i][j]
    if s == 2:
        pos = pos + 1

    # Check second diagonal for winning positions
    s = 0
    for i in range(LEN):
        for j in range(LEN):
            if i + j == LEN - 1:
                s = s + M[i][j]
    if s == 2:
        pos = pos + 1

    # If number of winning positions is 2 and more - there is a trap
    # If number of winning positions is 1 - there is a possible winning combination
    return pos >= lvl

def game_over(M):
    '''
    This function checks if the game is over
    - One of the gamers won
    - There is a game draw (no free cells)
    '''
    # Check horizontals
    for i in range(LEN):
        s = 0
        for j in range(LEN):
            s = s + M[i][j]
        if s == 3:
            print_matrix(M)
            print('You lost...')
            return True
        elif s == -3:
            print_matrix(M)
            print('You won!')
            return True

    # Check verticals
    for j in range(LEN):
        s = 0
        for i in range(LEN):
            s = s + M[i][j]
        if s == 3:
            print_matrix(M)
            print('You lost...')
            return True
        elif s == -3:
            print_matrix(M)
            print('You won!')
            return True

    # Check first diagonal
    s = 0
    for i in range(LEN):
        for j in range(LEN):
            if i == j:
                s = s + M[i][j]
    if s == 3:
        print_matrix(M)
        print('You lost...')
        return True
    elif s == -3:
        print_matrix(M)
        print('You won!')
        return True

    # Check second diagonal
    s = 0
    for i in range(LEN):
        for j in range(LEN):
            if i + j == LEN - 1:
                s = s + M[i][j]
    if s == 3:
        print_matrix(M)
        print('You lost...')
        return True
    elif s == -3:
        print_matrix(M)
        print('You won!')
        return True

    # Check if there are free cells
    for i in range(LEN):
        for j in range(LEN):
            if M[i][j] == 0:
                # There are fre cells - the game continues
                return False

    print_matrix(M)
    print('Draw in game')
    return True

def game_main(M, my):
    '''
    This is a main recursive function
     - It asks the gamer to do his move
     - It does own move
     - It checks if the game is over (and returns in this case)
     - It calls itself
    '''
    if my:
        M = my_turn(M)
    else:
        print_matrix(M)
        M = your_turn(M)
        if M is None:
            return

    # If the game is over - return
    if game_over(M):
        return

    # Recursive call
    game_main(M, not my)

# Main entry point for the game
if __name__ == '__main__':

    # Initialize the game
    M = init_game()

    if M is not None:
        # Start the loop
        game_main(M, MY_SIGN == 'X')

