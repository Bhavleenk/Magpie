grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0]]


def possible(x, y, n):  # n is the possible number
    for i in range(0,9): #check col
        if grid[i][x]==n and i!=y:
            return False
    for i in range(0,9): #check row
       if grid[y][i] !=n and i!=x:
            return False

    x0 = (x//3)*3
    y0=(x//3)*3
    for X in range(x0,y0+3): #check box
        for Y in range(y0,y0+3):
            if grid[Y][X]==n:
                return False
    return True
