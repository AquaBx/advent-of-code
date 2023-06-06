from operator import pos
from turtle import position


with open("./day10/data.txt") as file:
    fread = file.read().split("\n")

    state = {}
    iter = 0
    res = 1

    image = [["." for _ in range(40)] for _ in range (6)]
    position = 0

    for action in fread:
        iter += 1
        state[iter] = res
        action = action.split(" ")

        j = (iter-1)%40
        i = (iter-1)//40
        if j in range(position,position+3):
            image[i][j] = "#"
        else:
            image[i][j] = " "

        if action[0] == "addx":
            
            j = (iter)%40
            i = (iter)//40
            if j in range(position,position+3):
                image[i][j] = "#"
            else:
                image[i][j] = " "

            j = (iter+1)%40
            i = (iter+1)//40
            if j in range(position,position+3):
                image[i][j] = "#"
            else:
                image[i][j] = "."

            iter += 1

            

            state[iter] = res
            res += int(action[1])
            position += int(action[1])


    iter += 1
    state[iter] = res

    somme = 0
    for item in [20,60,100,140,180,220]:
        somme += state[item] * item 
    print(somme)

    for item in image :
        line= ""
        for char in item:
            line+=char
        print(line)