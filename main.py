
'''def multi_table(number):
    table = ''
    for i in range(10):
        row = f'{i + 1} * {number} = {(i + 1) * number}'
        if i + 1 != 10:
            table += row + '\n'
        else:
            table += row
    return table  # good luck


print(multi_table(4))'''  # Multiply table


dice = [1, 1, 5, 1, 5, 4]
board = [0, 0, 3, 0, 0, 0, -2, 0, 0, 0]

def snakes_ladder(dice: list, board: list):
    throws = 0
    position = 0
    while throws <= len(dice):
        for i in range(len(dice)):
            position += dice[i]
            throws += 1
            if board[position] + dice[i] > len(board) - board.count(board[:position]):
                pass
            elif board.index(board[position]) == board.index(board[-1]):  # PROBLEMS!!!!
                return board.index(board[-1])
            elif board[position] > 0:
                position += board[position]
            elif board[position] < 0:
                position -= board[position]
            elif board[position] == 0:
                pass





print(snakes_ladder(dice, board))