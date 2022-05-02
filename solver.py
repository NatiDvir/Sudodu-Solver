import random

bo = [
    [3, 0, 2, 0, 5, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 0, 0, 9, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 4, 3, 0, 0, 0, 7, 5, 0],
    [0, 9, 0, 0, 0, 4, 0, 0, 8],
    [4, 0, 9, 7, 0, 0, 0, 6, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 4, 0, 2, 0, 3]
]


def printBoard(board):
    """
        parameters: int board[9][9]
        prints the board
        return none
    """
    for i in range(len(board[0])):
        if i % 3 == 0 :
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ", end="")
            if j == 8:
                print(str(board[i][j]) + " |")
            else:
                print(str(board[i][j]) + " ", end="")
    print("- - - - - - - - - - - - -")


def emptyPosition(board):
    """
        parameters: int board[9][9]
        Find and return an empty position on board in coordinate of (x,y)
        return (x,y)
    """
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def checkRow(board, num, position):
    """
        parameters: (int board[9][9] , int num , int position[2])
        return bool
    """

    for i in range(len(board[0])):
        if num == board[position[0]][i] and position[1] != i:
            return False
    return True


def checkCol(board, num, position):
    """
        parameters: (int board[9][9] , int num , int position[2])
        return bool
    """
    for i in range(len(board[0])):
        if num == board[i][position[1]] and position[0] != i:
            return False
    return True


def checkBox(board, num, position):
    """
        parameters: (int board[9][9] , int num , int position[2])
        return bool
    """
    boxX = position[0] // 3
    boxY = position[1] // 3
    for i in range(boxX*3,boxX*3 + 3):
        for j in range(boxY*3,boxY*3 + 3):
            if num == board[i][j] and position != (i, j):
                return False
    return True


def checkValid(board, num, position):
    """
        parameters: (int board[9][9] , int num , int position[2])
        Check for num and position if row,col and box does not already contain the number.
        return bool
    """
    if checkBox(board, num, position) and checkCol(board, num, position) and checkRow(board, num, position):
        return True
    else:
        return False


def solve(board):
    """
        parameters: int board[9][9]
        find and solve the sudoku board input
        return solved board
    """
    pos = emptyPosition(bo)
    if not pos:  # If no empty place - board is full
        return True
    else:
        for i in range(1, 10):  # Check for all numbers 1-9 to fit
            if checkValid(bo, i, (pos[0], pos[1])):  # Check if number 'i' is a valid number.
                bo[pos[0]][pos[1]] = i
                if solve(bo):  # Recursive call to backtrack
                    return True
                bo[pos[0]][pos[1]] = 0  # If solution is wrong - delete number from position and try the next number.
        return False

def initBoard(new):
    """
           parameters: int board[9][9]
           return empty board
       """
    for i in range(9):
        for j in range(9):
            new[i][j] = 0
    return new


def sudokuGenerator(new):
    """
           parameters: int board[9][9]

           return new soduko board 
       """
    board = initBoard(new)

    numbers = 15
    numbersDone = 0

    while numbersDone < numbers:

        x = random.randint(1, 8)
        y = random.randint(1, 8)
        number = random.randint(1, 9)

        if board[x][y] == 0:
            board[x][y] = number
            if not checkValid(board,number,(x,y)):
                board[x][y] = 0
            else:
                numbersDone += 1

    return board


done = True
new = bo
printBoard(bo)
while done :
    print("Press 1 to solve! \nPress 2 for a new board! \n")
    user = input()
    if user == '1' : break
    if user == '2' :
        new = sudokuGenerator(bo)
        printBoard(new)
        print("Board Rotated!")
    else: break

solve(new)
printBoard(new)
