#Eric Wright
#12/18
#tic-tac-toe

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
    """Display game instructions."""
    print(
    """
    Hi user you suck. Want to play my game???
    Here are your instructions:
    To the things and stuff you need to win
    Just kidding
    Here are your real instructions:
    To place a 'X' or an 'O' you need to enter in the number posision of 0-8 for where you want to place your 'X' or 'O'
    Here are the posisions:
        -------------
        | 0 | 1 | 2 |
        | --------- |
        | 3 | 4 | 5 |
        | --------- |
        | 6 | 7 | 8 |
        | --------- |
        -------------
    To win the game you need to get three in a row.
    Good Luck....
    I'm going to win because I have a far superior intelect compaired to you
    """
    )

def ask_yes_no(question):
    """Ask a yes or no question."""
    responce = None
    ANSWER = ("y", "n")
    while responce not in ANSWER:
        print(question)
        responce = input("y or n ").lower()
    return responce

# Test ask_yes_no()
# x = ask_yes_no("do you like this class")
# print(x)

def ask_number(question, low, high):
    """Ask fo a number within a range."""
    responce = "99999"
    while True:
        if responce.isdigit():
            if int(responce) in range(low, high):
                break
            else:
                responce = input(question)
        else:
            print("you must enter a number")
            responce = input(question)
    return int(responce)

# Test ask_number()
# x = ask_number("enter a number between 1 and 10 ",1,11)
# print(x)

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human

# Test pieces()
# com, human = pieces()

# print(com)
# print(human)

def new_board():
    """Create new game board."""
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# Test new_board()
# x = new_board()
# print(x)
 
def display_board(board):
    """Display game board on screen."""
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Test display_board()
# x = new_board()
# display_board(x)

def legal_moves(board):
    """Creates list of legal moves."""
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

# Test legal_moves()
# x = new_board()
# display_board(x)
# moves = legal_moves(x)
# print(moves)

def winner(board):
    """Dertermine the game winner."""
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
        )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    
    return None

# Test winner()
# x = [X, X, X, " ", " ", " ", " ", " ", " "]
# display_board(x)

# winner = winner(x)
# print(winner)

def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move

# Test human_move()
# x = new_board()
# c, h = pieces()
# placement = human_move(x,h)
# print(placement)

def next_turn(turn):
    """Swich turns."""
    if turn == X:
        return O
    else:
        return X

# Test next_turn()
# turn = X
# turn = next_turn(turn)
# print(turn)

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won\n")
    else:
        print("Its a tie:\n")
    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n"\
        "Proof that computers are superion to humans in all regards.")
    elif the_winner == human:
        print("No, no! It connot be! Somehow you tricked me, human. \n"\
        "But never again! I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n"\
        "Celebrate today... for this is the best you will ever achieve.")

# Test congrat_winner()
# h = X
# c = O
# w = TIE
# congrat_winner(w,c,h)

def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with cince function will changeing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take quare number", end=" ")
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    #if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def main():
    """Main function for the game."""
    display_instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
            display_board(board)
            turn = next_turn(turn)
        elif turn == computer:
            move = computer_move(board, computer, human)
            display_board(board)
            turn = next_turn(turn)
    theWinner = winner(board)
    congrat_winner(theWinner, computer, human)
main()