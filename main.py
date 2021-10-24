board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
board_ref = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):
    pos = find_empty(bo)
    #print(bo)
    if not pos:
        return True
    else:
        row = pos[0]
        col = pos[1]
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            else:
                bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if pos[1] != i and num == bo[pos[0]][i]:
            return False
    # check column
    for i in range(len(bo)):
        if pos[0] != i and num == bo[i][pos[1]]:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if (i, j) != pos and num == bo[i][j]:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == len(bo[0]) - 1:
                print(bo[i][j])
            else:
                print(f"{bo[i][j]}", end=" ")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


print_board(board)
#print(valid(board,6,(0,8)))
solve(board)
print("\n")
if board == board_ref:
    print("not solvable")
else:
    print_board(board)
