import unittest

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
etape = 0
fini = False
def dist(grid):
    global startp,endp,setdistance,setcconnueparalgo
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
    global setdistance
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
    global cact
    if not algo_a_commencer:
        cact = startp
        grid[cact[0]][cact[1]] = "T"
    else:
        grid[cact[0]][cact[1]] = "T"

def voisin(grid,cact):
    cellule = grid[cact[1]][cact[0]]
    global dstvoisinup,dstvoisindown,dstvoisinleft,dstvoisindroite,lstdst,meilleur
    listmeilleur = {}
    if cact[1]-1 >= 0:
        voisinup = (cact[0],cact[1]-1)
        dstvoisinup = setdistance[voisinup]
        listmeilleur[voisinup] = dstvoisinup
    else:
        voisinup = None
    if cact[1]+1 < len(grid):
        voisindown = (cact[0],cact[1]+1)
        dstvoisindown = setdistance[voisindown]
        listmeilleur[voisindown] = dstvoisindown
    else:
        voisindown = None
    if cact[0]-1>= 0:
        voisinleft = (cact[0]-1,cact[1])
        dstvoisinleft = setdistance[voisinleft]
        listmeilleur[voisinleft] = dstvoisinleft
    else:
        voisinleft = None
    if cact[0]+1 < len(grid[cact[1]]):
        voisindroite = (cact[0]+1,cact[1])
        dstvoisindroite = setdistance[voisindroite]
        listmeilleur[voisindroite] = dstvoisindroite
    else:
        voisindroite = None
    minval = None
    meilleur = None
    for i,j in listmeilleur:
        if minval == None or minval > j:
            minval = j 
            meilleur = i

def algo(grid):
    global etape,fini,cact
    algo_a_commencer = True
    cact = meilleur


dist(grid)
dist_chaque_cellule(grid)
while not fini :
    celluleactuelle(grid)
    voisin(grid,cact)
    algo(grid)



class TestAbsFunction(unittest.TestCase):
    pass
