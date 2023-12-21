import random
def display_board(board):
    print("\n" * 10)
    for x in range(len(board)):
        res = "\t\t\t"
        for i in range(len(board)):
            res += str(board[x][i])
            if i <len(board)-1: res += "\t,\t"
        print(res)
        if x < len(board)-1:
            print("\t",("\t-\t"*4))
        else:
            pass

def player_input():
    print("\n")
    position = input("Enter Move (8=u,2=d,6=r,4=l): ")
    list = [8,6,4,2]
    while int(position) not in list:
        print("Invalid position!" "\n" )
        position = input("Enter Direction (8 = up, 2 = down, 6 = right, 4 = left): ")
    return int(position)

def multiply(num):
    num = num*2

def is_emptyi(board):
    listi = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                listi.append(i)
    return listi
def is_emptyj(board):
    listj = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                listj.append(j)
    return listj

def Move_down(board):
    mylist = [3,2,1,0]
    mylist1 = [1,2,3]
    for _ in range(len(board)-1):
        for i in mylist:
            for j in mylist1:
                if board[j][i] == ".":
                    board[j][i] = board[j - 1][i]
                    board[j - 1][i] = "."
                elif board[j][i] == board[j - 1][i]:
                    board[j][i] = board[j][i] * 2
                    board[j - 1][i] = "."


def Move_up(board):
    for _ in range(len(board)):
        for i in range(len(board)):
            for j in range(len(board)-1):
                if board[j][i] == ".":
                    board[j][i] = board[j+1][i]
                    board[j + 1][i] = "."
                elif board[j][i] == board[j+1][i]:
                    board[j][i] = board[j][i] * 2
                    board[j+1][i] = "."

def Move_left(board):
    mylist = [2, 1, 0]
    mylist1 = [0, 1, 2]
    for _ in range(len(board)):
        for i in range(len(board)):
            for j in mylist1:
                if board[i][j] == ".":
                    board[i][j] = board[i][j+1]
                    board[i][j+1] = "."
                else:
                    if board[i][j+1] == board[i][j]:
                        board[i][j] = board[i][j] * 2
                        board[i][j + 1] = "."



def Move_right(board):
    for _ in range(len(board)):
        for i in range(len(board)):
            for j in range(len(board)-1):
                if board[i][j+1] == ".":
                    board[i][j + 1] = board[i][j]
                    board[i][j] = "."
                else:
                    if board[i][j] == board[i][j+1]:
                        board[i][j] = board[i][j] * 2
                        board[i][j+1] = "."

def generate_num(board, i, j):
    id = random.choice(i)
    jd = random.choice(j)
    while board[id][jd] != ".":
        id = random.choice(i)
        jd = random.choice(j)
    board[id][jd] = random.choice([2,4])

def is_over(board):
    return False

board = [[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
generate_num(board, is_emptyi(board), is_emptyj(board))
generate_num(board, is_emptyi(board), is_emptyj(board))
for _ in range(100):
    display_board(board)
    direction = player_input()
    if direction == 8:
        Move_up(board)
    elif direction == 2:
        Move_down(board)
    elif direction == 6:
        Move_right(board)
    elif direction == 4:
        Move_left(board)
    generate_num(board, is_emptyi(board), is_emptyj(board))


display_board([])