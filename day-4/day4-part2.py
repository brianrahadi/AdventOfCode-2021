list = [x for x in open("day4-input.txt").read().strip().split("\n")]

answer = list[0].split(',')

row, col = 0, 0
boards = []
markeds = []

for line in range(2, len(list), 6):
    board = []
    marked = []
    row = (line - 2) // 5
    for col in range(5):
        board.append(list[line+col].split())
        marked.append([False] * 5)
    markeds.append(marked)
    boards.append(board)

def check_board_row(markeds, numBoard, row):
    for i in range(5):
        if not (markeds[numBoard][row][i]):
            return False
    return True

def check_board_col(markeds, numBoard, col):
    for i in range(5):
        if not (markeds[numBoard][i][col]):
            return False
    return True

def countNum(board, marked):
    num = 0
    for row in range(5):
        for col in range(5):
            if not marked[row][col]:
                num += int(board[row][col])
    return num

def printBoard(board, numBoard):
    for row in range(5):
        for col in range(5):
            print(board[numBoard][row][col], end = ' ')
        print()
        
def play():
    counter = 0
    set = {}
    for ans in answer:
        for numBoard in range(len(boards)):
            for row in range(5):
                for col in range(5):
                    if boards[numBoard][row][col] == ans:
                        markeds[numBoard][row][col] = True
            for diag in range(5):
                if (numBoard not in set and (check_board_row(markeds, numBoard, diag) or (check_board_col(markeds, numBoard, diag)))):
                    set[numBoard] = True
                    print(countNum(boards[numBoard], markeds[numBoard]) * int(ans))

play() 
## last board is 3178

