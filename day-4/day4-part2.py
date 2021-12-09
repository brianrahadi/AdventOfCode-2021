
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

def check_board_row(markeds, numBoard, row, col):
    for i in range(5):
        if not (markeds[numBoard][row][col+i]):
            return False
    return True

def check_board_col(markeds, numBoard, row, col):
    for i in range(5):
        if not (markeds[numBoard][row+i][col]):
            return False
    return True

def mark_board(num, boards, markeds, numBoard, row, col):
    if boards[numBoard][row][col] == num:
        markeds[numBoard][row][col] = True

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
    for ans in answer:
        for numBoard in range(len(boards)):
            for row in range(5):
                for col in range(5):
                    if boards[numBoard][row][col] == ans:
                        markeds[numBoard][row][col] = True
            for diag in range(5):
                if (check_board_row(markeds, numBoard, diag, 0) or (check_board_col(markeds, numBoard, 0, diag))):
                    if (counter < 99):
                        counter += 1
                    else:
                        return countNum(boards[numBoard], markeds[numBoard]) * int(ans)
print(play())