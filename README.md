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
