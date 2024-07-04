
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
    setdistance[(x,y)] = dist
    setdistance[(xe,ye)] = 0
    setcconnueparalgo["S"] = dist 
    setcconnueparalgo["E"] = 0

def dist_chaque_cellule(grid):
    global setdistance
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "O":
                count += 1
                xo = j
                yo=i 
                dist = abs(xo-endp[0])+abs(yo-endp[1])
                setdistance[(xo,yo)] = dist

def celluleactuelle(grid,startp):
    global cact
    if not algo_a_commencer:
        cact = startp
    grid[cact[0]][cact[1]] = "T"

def voisin(grid):
    global meilleur,minval
    listmeilleur = dict()
    if cact[1]-1 >= 0:
        voisinup = (cact[0],cact[1]-1)
        dstvoisinup = setdistance[voisinup]
        listmeilleur[voisinup] = dstvoisinup

    if cact[1]+1 < len(grid):
        voisindown = (cact[0],cact[1]+1)
        dstvoisindown = setdistance[voisindown]
        listmeilleur[voisindown] = dstvoisindown

    if cact[0]-1>= 0:
        voisinleft = (cact[0]-1,cact[1])
        dstvoisinleft = setdistance[voisinleft]
        listmeilleur[voisinleft] = dstvoisinleft

    if cact[0]+1 < len(grid[cact[1]]):
        voisindroite = (cact[0]+1,cact[1])
        dstvoisindroite = setdistance[voisindroite]
        listmeilleur[voisindroite] = dstvoisindroite

    
    for key,value in listmeilleur.items():
        if minval == None or value < minval:
            minval = value
            meilleur = key
    return meilleur

def algo(grid):
    global etape,fini,cact,algo_a_commencer
    algo_a_commencer = True
    cact = meilleur
    etape+=1
    print(cact)
    if grid[cact[1]][cact[0]] == "E":
        fini = True
        print(affichgrille(grid))
    print(" nombre d'étape : {}".format(etape))

def affichgrille(grid):
    strgrille = ""
    for i in grid:
        strgrille = strgrille + str(i) + "\n"    
    return strgrille


def main():
    grid= [ ["S","O","O"],
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
    meilleur = None
    minval = None
    dist(grid)
    dist_chaque_cellule(grid)
    while not fini :
        celluleactuelle(grid,startp)
        voisin(grid)
        algo(grid)



