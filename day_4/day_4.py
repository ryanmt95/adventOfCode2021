def giant_squid(bingo_numbers, boards):
    
    board_maps = build_board_maps(boards)
    
    bingo_tracker = []
    for board_map in board_maps:
        bingo_tracker.append(winning_index(bingo_numbers, board_map))

    first_bingo_index = min(bingo_tracker)
    index = bingo_tracker.index(first_bingo_index)

    return find_score(board_maps[index], bingo_numbers, first_bingo_index)

def dont_eat_me_squid(bingo_numbers, boards):
    
    board_maps = build_board_maps(boards)
    bingo_tracker = []
    for board_map in board_maps:
        bingo_tracker.append(winning_index(bingo_numbers, board_map))
    
    last_bingo_index = max(bingo_tracker)
    index = bingo_tracker.index(last_bingo_index)

    return find_score(board_maps[index], bingo_numbers, last_bingo_index)

def find_score(board, bingo_numbers, bingo_index):
    marked_numbers = [0 if num not in board else num for num in bingo_numbers[:bingo_index+1]]
    total = sum(board.keys()) - sum(marked_numbers)
    return total * bingo_numbers[bingo_index]

def winning_index(bingo_numbers, board_map):

    bingos_tracker = [[5 for _ in range(5)] for _ in range(2)]

    for bingo_index, bingo_num in enumerate(bingo_numbers):
        if bingo_num in board_map:
            row, col = board_map[bingo_num]
            bingos_tracker[0][row] -= 1
            bingos_tracker[1][col] -= 1

            if bingos_tracker[0][row] == 0:
                return bingo_index
            elif bingos_tracker[1][col] == 0:
                return bingo_index
    
    return 0

def build_board_maps(boards):
    board_maps = []
    for board in boards:
        board_map = dict()
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                board_map[num] = (i, j)
        
        board_maps.append(board_map)
    
    return board_maps

if __name__ == "__main__":
    print("Day 4 and 9 more days to Germany")

    f = open("day_4.txt",'r',encoding = 'utf-8')

    bingo_numbers = list(map(int, f.readline().replace("\n", "").split(",")))
    f.readline()

    boards = []
    board = []
    for row in f:
        row = row.replace("\n", "").strip()
        if row == "":
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, row.split())))
    
    boards.append(board)

    result = giant_squid(bingo_numbers.copy(), boards.copy())
    print(result)

    result2 = dont_eat_me_squid(bingo_numbers.copy(), boards.copy())
    print(result2)
