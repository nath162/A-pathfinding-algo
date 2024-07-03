

grid= [ ["S","O","0"],
        [ "O","O","O"],
        [ "O","O","E"],
        ]
def dist(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] =="S":
                x = j
                y = i
            elif grid[i][j] == "E":
                xe = j
                ye = i  
    return abs(x-xe)+abs(y-ye)
print(dist(grid))