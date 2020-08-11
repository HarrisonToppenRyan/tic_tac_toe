
# Game still running
game_still_runs = True

#Whomstve won? or Draw?
winner = None

# Who's turn is it?
current_player = "X"

# The Game Board 
main_board = ["-", "-", "-", 
          "-", "-", "-",
          "-", "-", "-"]

def show_board():
    print(main_board[0] + " | " + main_board[1] + " | " + main_board[2])
    print(main_board[3] + " | " + main_board[4] + " | " + main_board[5])
    print(main_board[6] + " | " + main_board[7] + " | " + main_board[8])

# Tic Tac Toe Game
def Start_game():
    
    # Display initial board 
    display_main_board()

    while game_still_runs:
        
        handle_turn(current_player)

        check_if_game_finished()

        change_player()

    # Game Over 
    if winner == "X" or winner == "O":
        print(winner + " was Victorious.")
    elif winner == None:
        print("The game is a Draw.")
    

def handle_turn(player):
    position = input("Choose a position from on the main board: ")
    position = int(position) - 1

    main_board[position] = player

    display_main_board()

def check_if_game_finished():
    check_if_win()
    check_if_draw()


def check_if_win():
    global winner 

    row_winner = check_rows()

    col_winner = check_col()

    diag_winner = check_diag()
    if row_winner:
        # row winner 
        winner = row_winner
    elif col_winner:
        # column winner 
        winner = col_winner
    elif diag_winner:
        # diagonal winner
        winner = diag_winner
    else: 
        #there was no win
        winner = None 

def check_rows():
    global game_still_runs
    row_1 = main_board[0] == main_board [1] == main_board[2] != "-"
    row_2 = main_board[3] == main_board [4] == main_board[5] != "-"
    row_3 = main_board[6] == main_board [7] == main_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_runs = False
    if row_1:
        return main_board[0]
    elif row_2:
        return main_board[3]
    elif row_3:
        return main_board[6]
    return None

def check_columns():
    global game_still_runs
    col_1 = main_board[0] == main_board [3] == main_board[6] != "-"
    col_2 = main_board[1] == main_board [4] == main_board[7] != "-"
    col_3 = main_board[2] == main_board [5] == main_board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_runs = False
    #Return winner 
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return None

def check_diag():
    global game_still_runs 
    diag_1 = main_board[0] == main_board [4] == main_board[8] != "-"
    diag_2 = main_board[6] == main_board [4] == main_board[2] != "-"
    
    if diag_1 or diag_2:
        game_still_runs = False
    if diags_1:
        return main_board[0]
    elif diag_2:
        return main_board[2]
    return None

def check_if_draw():
    global game_still_runs

    if "-" not in main_board:
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
    
