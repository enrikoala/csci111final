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

initialize()

# Def places coordinates (starting, ending, and all other points)
#Def World rules/how its suppose to move 
#Def Utility
# Def its action plan?