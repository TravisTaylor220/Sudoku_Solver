##This is a sudoku solver
table = [
    [6,7,0,0,0,0,0,5,1],
    [0,0,0,8,0,0,0,0,6],
    [0,0,0,2,0,0,4,0,0],
    [0,9,1,0,0,0,0,0,8],
    [7,0,0,0,0,5,0,0,0],
    [0,0,5,6,0,3,1,0,0],
    [0,0,0,1,0,2,0,0,0],
    [0,1,0,0,9,0,7,3,0],
    [0,0,3,7,0,0,0,0,0]
    ]

def solve(tab):

    find = find_spaces(tab)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(tab, i, (row, col)):
            tab[row][col] = i

            if solve(tab):
                return True
            
            tab[row][col] = 0
        
    return False



def valid(tab, num, pos):
    #checks row
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    #checks column
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False
    
    #checks box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if tab[i][j] == num and (i,j) != pos:
                return False

    return True

def print_table(tab):

    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print (tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")
                

def find_spaces(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0: 
                return(i, j) # row, column

    return None

def puzzle_ans(ans):
    if ans == 'Y':
        print()
        print_table(table)
    else:
        ans = input("Please press (Y) when you are ready to see the completed table --- ")
        print()
        puzzle_ans(ans)
print_table(table)
solve(table)
print()
ans = input("Do you wish to see the solved puzzle? (Y/N) ")
puzzle_ans(ans)

