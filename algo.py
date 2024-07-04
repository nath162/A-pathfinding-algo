setdistance = dict()
startp=()
possible =True
endp =()
algo_a_commencer = False
cact = ()
setcconnueparalgo = {}
etape = 0
fini = False
meilleur = None
minval = None
def dist(grid):
    global startp,endp,setdistance,setcconnueparalgo
    for i in range(len(grid)):
        for j in range(len(grid[i])):
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
    setcconnueparalgo[(x,y)] = dist 
    setcconnueparalgo[(xe,ye)] = 0

def dist_chaque_cellule(grid):
    global setdistance
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
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
    global meilleur,minval,possible
    listmeilleur = dict()
    if cact[1]-1 >= 0:
        voisinup = (cact[0],cact[1]-1)
        if grid[cact[0]][cact[1]-1] == "O" or grid[cact[0]][cact[1]-1] == "E":
            dstvoisinup = setdistance[voisinup]
            listmeilleur[voisinup] = dstvoisinup
            setcconnueparalgo[voisinup] = dstvoisinup

    if cact[1]+1 < len(grid):
        voisindown = (cact[0],cact[1]+1)
        if grid[cact[0]][cact[1]+1] == "O" or grid[cact[0]][cact[1]+1] == "E":
            dstvoisindown = setdistance[voisindown]
            listmeilleur[voisindown] = dstvoisindown
            setcconnueparalgo[voisindown] = dstvoisindown

    if cact[0]-1>= 0:
        voisinleft = (cact[0]-1,cact[1])
        if grid[cact[0]-1][cact[1]] == "O" or grid[cact[0]-1][cact[1]] == "E":
            dstvoisinleft = setdistance[voisinleft]
            listmeilleur[voisinleft] = dstvoisinleft
            setcconnueparalgo[voisinleft] = dstvoisinleft

    if cact[0]+1 < len(grid[cact[1]]):
        voisindroite = (cact[0]+1,cact[1])
        if grid[cact[0]+1][cact[1]] == "O" or grid[cact[0]+1][cact[1]] == "E":
            dstvoisindroite = setdistance[voisindroite]
            listmeilleur[voisindroite] = dstvoisindroite
            setcconnueparalgo[voisindroite] = dstvoisindroite

    if listmeilleur == {} and setcconnueparalgo == {}:#par contre si il connait une possibilité il faut qu'il y retourne et trouve un autre chemin apartir de cette cellule
        possible = False
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
    print(" nombre d'étape : {}".format(etape))
    print(cact)
    if grid[cact[1]][cact[0]] == "E":
        fini = True
        print(affichgrille(grid))

def affichgrille(grid):
    strgrille = ""
    for i in grid:
        strgrille = strgrille + str(i) + "\n"    
    return strgrille

def main():
    grid= [ ["S","O","X","E"]]

    dist(grid)
    dist_chaque_cellule(grid)
    celluleactuelle(grid,startp)
    while not fini and possible:
        voisin(grid)
        algo(grid)
        celluleactuelle(grid,startp)
if __name__ == "__main__":
    main()
