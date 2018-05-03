def print_picture(picture):
    len_x = len(grid[:][0]) 
    len_y = len(grid)
    for i in range(len_x):
        for y in range(len_y):
            print(picture[y][i], end='')
            if y == len_y-1:
                print('\n')
            
            

    


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print_picture(grid)
