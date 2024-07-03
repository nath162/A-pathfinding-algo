grid= [ ["S","O","0"],
        [ "O","O","O"],
        [ "O","O","E"],
        ]

setdistance = dict()
startp=()
endp =()
algo_a_commencer = False
cact = ()
setcconnueparalgo = {}

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
    setdistance["S"] = dist
    setdistance["E"] = 0
    setcconnueparalgo["S"] = dist 
    setcconnueparalgo["E"] = 0

def dist_chaque_cellule(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "O":
                count += 1
                xo = i
                yo=j 
                dist = abs(xo-endp[0])+abs(yo-endp[1])
                setdistance[(xo,yo)] = dist

def celluleactuelle(grid):
    if not algo_a_commencer:
        cact = startp

def voisin(grid,cact):
    cellule = grid[cact[1]][cact[0]]
    try:
        voisinup = (cact[1]+1,cact[0])
        dstvoisinup = setdistance[voisinup]
    except IndexError:
        pass
    try:
        voisindown = (cact[1]-1,cact[0])
        dstvoisindown = setdistance[voisindown]
    except IndexError:
        pass
    try:
        voisinleft = (cact[1],cact[0]-1)
        dstvoisinleft = setdistance[voisinleft]
    except IndexError:
        pass
    try:
        voisindroite = (cact[1],cact[0]+1)
        dstvoisindroite = setdistance[voisindroite]
    except IndexError:
        pass

def algo(grid):
    pass

dist(grid)
print(dist_chaque_cellule(grid))
