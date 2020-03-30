board = [
         [2,0,3,8,0,0,0,0,0],
         [0,9,0,4,0,0,3,6,0],
         [5,0,0,0,6,3,0,2,0],
         [6,0,7,0,0,0,0,9,8],
         [0,0,5,9,0,0,0,1,6],
         [4,0,0,0,7,0,2,0,3],
         [0,0,0,3,0,4,0,0,0],
         [0,0,0,0,2,0,0,0,0],
         [0,0,8,0,0,0,0,0,0]
]

def pretty_print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j, col in enumerate(row):
            if j == 8:
                print(str(board[i][j]) + " ", end="")
                print("|")
            elif j % 3 == 0:
                print("| ", end="")
                print(str(board[i][j]) + " ", end="")
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                print(i, j)
                return i, j
    return None

# check if number if valid at certain position on the board
def is_valid(board, num, pos):
    if not check_col(board, num, pos):
        return False
    elif not check_row(board, num, pos):
        return False
    elif not check_square(board, num, pos):
        return False
    return True

def check_square(board, num, pos):
    square_pos = (pos[0]//3*3, pos[1]//3*3)
    for i in range(square_pos[0], square_pos[0]+3):
        for j in range(square_pos[1], square_pos[1]+3):
            if (i,j) != pos and num == board[i][j]:
                print("False => " + str((i, j)))
                return False
    return True

def check_row(board, num, pos):
    for i in range(len(board[0])):
        if num == board[pos[0]][i] and (pos[0],[i]) != pos:
            print("False => " + str((pos[0],i)))
            return False
    return True

def check_col(board, num, pos):
    for j in range(len(board)):
        if num == board[j][pos[1]] and (j,pos[1]) != pos:
            print("False => " + str((j, pos[1])))
            return False
    return True

def solve(board):
    first_empty = find_empty_square(board)
    # base case: finished filling the board
    if not first_empty:
        return True
    else:
        row, col = first_empty

    for i in range(1,10):
        print("for " + str(i))
        if is_valid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

solve(board)
pretty_print_board(board)