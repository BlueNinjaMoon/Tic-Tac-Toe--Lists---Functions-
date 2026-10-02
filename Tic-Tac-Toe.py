def print_board(board):
    """"Prints the Tic-Tac-Toe board, with any moves made by the Playermoves function."""
    print(f"_{board[0]}_|_{board[1]}_|_{board[2]}_")
    print(f"_{board[3]}_|_{board[4]}_|_{board[5]}_")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def player_move(pl:str) -> int:
    """Asks player  which spot they will put X/O in."""
    userin = input(f"Where will {pl} be placed (pick 1-9)")
    userin = checkmove(userin)
    return userin -1
              
def checkmove(pl):
    """The players move will be checked and make sure they can play the move there."""
    while pl.isdigit() != True:
        print("Invalid input.")
        pl = input("Enter a number 1 through 9: ")
    pl = int(pl)
    while not 0 <= pl <= 8:
        print("Invalid move spot.")
        pl = input("Enter a number within the range of 1 through 9: ")
    pl = int(pl)
    return pl

def checktie():
    """It will check to see if the game is a tie at the end."""
    # if move == 0 and check.count("X") == 5:
    #     print("You guys tied!")
    # elif move == 8 and check.count("X") != 5:
    #     None

    ####alt approach####
    for space in board:
        if space not in ["X","O"]:
            return False #found open space
    return True

def checkwin():
    """It will check who won and where they won."""
    #checktie(check, move)
    #check rows:
    for i in range(0,9,3):
        if board[i] == board[i+1] == board[i+2] and board[i] in ["X","O"]:
            return board[i]
    #check cols
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] in ["X","O"]:
            return board[i]
    #check diagonal:

    return None

def playagain(PLinput):
    """It will reset the board if the player is playing again, or end the game."""
    PLinput = input("Would you like to play again? (Y/y for yes, N/n for No): ").strip.lower()
    if PLinput == "y":
            PLinput.clear()
            return PLinput
    else:
        if PLinput != "n":
            print("Invalid input!")
        else:
            None
             
def reset_board(reset):
    """It will reset the board if the player is playing again."""
    if reset == True:
        board = ["_1_|", "_2_", "|_3_", "_4_|", "_5_", "|_6_", " 7 |", " 8 ", "| 9"]
    else:
        None

# board = ["_1_|", "_2_", "|_3_", "_4_|", "_5_", "|_6_", " 7 |", " 8 ", "| 9"]
board = [1,2,3,4,5,6,7,8,9]
# boardmove = 8
# player1 = "Where will X be placed?(1 through 9): "
# player2 = "Where will O be placed?(1 through 9): "
active_player = "X"
while True:
    while True:
        print_board(board)
        move = player_move(active_player)
        board[move] = active_player
        winner = checkwin()
        if winner:
            print(f"{winner} won!")
        elif checktie():
            print(f"It's a tie!")
            break
        active_player = "O" if active_player == "X" else "X"
    if playagain() == True:
        break
    else:
        reset_board()
