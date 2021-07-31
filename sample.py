import sys
ROWS=4

def initialize():
    grid=[]
    for r in range (0,ROWS,1):
        grid.append([])
    grid[0]=['','#',' ','#']
    grid[1]=['#','#',' ','#']
    grid[2]=['#','#',' ','#']
    grid[3]=['#','#',' ','#']
    
    row, col = 0, 2
    grid[row][col] = '0'
    print(grid)
    return grid, row, col


def move(grid, oldrow, oldcol, newrol, newcol):
    grid[oldrow][oldcol] = ' '
    grid[newrol][newcol] = 'O'

def main():
    grid, row, col = initialize()
    while True:
        display(grid)
        dir = input("Which way? ")
        if dir == '2':
            # move up, make sure to handle errors
        elif dir == '4':
            # move left
        # ditto for 6 and 8
        else:
            print("That's not a direction. Try 2, 4, 6, or 8.")

initialize()

# Def places coordinates (starting, ending, and all other points)
#Def World rules/how its suppose to move 
#Def Utility
# Def its action plan?