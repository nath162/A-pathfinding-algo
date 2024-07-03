grid= [ ["S","O","0"],
        [ "O","O","O"],
        [ "O","O","E"],
        ]
setdistance = set()
startp=()
endp =()
algo_a_commencer = False
cact = ()
def dist(grid):
    global startp,endp
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] =="S":
                x = j
                y = i
            elif grid[i][j] == "E":
                xe = j
                ye = i
    startp =(x,y)
    endp = (xe,ye)  
    dist = abs(x-xe)+abs(y-ye)
    setdistance.add(("S",dist))
    setdistance.add(("E",0))
    print(endp)

def dist_chaque_cellule(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "O":
                count += 1
                xo = i
                yo=j 
                dist = abs(xo-endp[0])+abs(yo-endp[1])
                setdistance.add(("o"+str(count),dist))
def celluleactuelle(grid):
    if not algo_a_commencer:
        cact = startp
def voisin(grid):
    pass

dist(grid)
print(dist_chaque_cellule(grid))
