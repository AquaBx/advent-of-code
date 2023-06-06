with open("./day8/data.txt") as file:
    fread = file.read().split("\n")
    foret = [ [int (a) for a in row] for row in fread]

    counter = 0

    foret_w = len(foret[0])
    foret_h = len(foret)

    for i in range(1, foret_h - 1 ):
        for j in range(1, foret_w - 1 ):

            visible = [True for i in range(4)]

            # visible a gauche
            for k in range(0,j):
                if foret[i][j] <= foret[i][k]:
                    visible[0] = False
                    break

            # visible a droite
            for k in range(j+1,foret_w):
                if foret[i][j] <= foret[i][k]:
                    visible[1] = False
                    break
            
            # visible en haut
            for k in range(0,i):
                if foret[i][j] <= foret[k][j]:
                    visible[2] = False
                    break
            
            # visible en bas
            for k in range(i+1,foret_h):
                if foret[i][j] <= foret[k][j]:
                    visible[3] = False
                    break
            
            if( visible.count(False) < 4  ): counter+=1


    print(counter + foret_h*2 + foret_w*2 - 4 )

    view = []

    for i in range(1, foret_h - 1 ):
        for j in range(1, foret_w - 1 ):

            visible = [0 for i in range(4)]

            # visible a gauche
            for k in range(j-1,-1,-1):
                visible[0] += 1
                if foret[i][j] <= foret[i][k]:
                    break

            # visible a droite
            for k in range(j+1,foret_w):
                visible[1] += 1
                if foret[i][j] <= foret[i][k]:
                    break
            
            # visible en haut
            for k in range(i-1,-1,-1):
                visible[2] += 1
                if foret[i][j] <= foret[k][j]:
                    break
            
            # visible en bas
            for k in range(i+1,foret_h):
                visible[3] += 1
                if foret[i][j] <= foret[k][j]:
                    break
            
            view.append(visible[0]*visible[1]*visible[2]*visible[3])

    print( max(view) )
