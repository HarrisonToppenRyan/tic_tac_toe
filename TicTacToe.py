#Game Board 
board = ["-", "-", "-", 
          "-", "-", "-",
          "-", "-", "-"]

# Game still going
game_still_runs = True

#Whomstve won? or Draw?
winner = None

# Who's turn is it?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Tic Tac Toe Game
def play_game():
    
    # Display initial board 
    display_board()

    while game_still_runs:
        
        handle_turn(current_player)

        check_if_game_finished()

        change_player()

    # Game End
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("The game is a Draw.")
    

def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = player

    display_board()

def check_if_game_finished():
    check_if_win()
    check_if_draw()


def check_if_win():

    #Sets up variables 
    global winner 


    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else: 
        #there was no win
        winner = None 

def check_rows():
    global game_still_runs
    #check is any rows are all same and not empty 
    row_1 = board[0] == board [1] == board[2] != "-"
    row_2 = board[3] == board [4] == board[5] != "-"
    row_3 = board[6] == board [7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_runs = False
    #Return winner 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return None

def check_columns():
    global game_still_runs
    #check is any rows are all same and not empty 
    column_1 = board[0] == board [3] == board[6] != "-"
    column_2 = board[1] == board [4] == board[7] != "-"
    column_3 = board[2] == board [5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_runs = False
    #Return winner 
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return None

def check_diagonals():
    global game_still_runs
    #check is any rows are all same and not empty 
    diagonals_1 = board[0] == board [4] == board[8] != "-"
    diagonals_2 = board[6] == board [4] == board[2] != "-"
    
    if diagonals_1 or diagonals_2:
        game_still_runs = False
    #Return winner 
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return None

def check_if_draw():
    global game_still_runs

    if "-" not in board:
        game_still_runs = False 
        return True
    else:
        return False

def change_player():
    #Player turns changing 
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    

play_game()
    