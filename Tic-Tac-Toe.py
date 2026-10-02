def print_board(board):
    """"Prints the Tic-Tac-Toe board, with any moves made by the Playermoves function."""
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def player_move(pl:str, board:int, move) -> str:
    """Asks player  which spot they will put X/O in."""
    pl = input(pl)
    pl -= 1
    move -= 1
    checkmove(pl, board)
              
def checkmove(pl, check):
    """The players move will be checked and make sure they can play the move there."""
    while pl.isdigit() != True:
        print("Invalid input.")
        pl = input(pl)
    while not 0 <= pl <= 8:
        print("Invalid move spot.")
        pl = input(pl)
    pl = int(pl)

def checktie(check, move):
    """It will check to see if the game is a tie at the end."""
    if move == 0 and check.count("X") == 5:
        print("You guys tied!")
    elif move == 8 and check.count("X") != 5:
        None

def checkwin(check, move):
    """It will check who won and where they won."""
    checktie(check, move)
    if board[0] == board[1] == board[2] and board[0] in ["X","O"]:
        return board[0]

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
        board = ["_1_|", "_2_", "|_3_", "_4_|", "_5_", "|_6_", "7  |", "8", "|  9"]
    else:
        None

