
with open("data.txt") as file:
    data = [[ ord(game[0])-ord("A") ,  ord(game[2])-ord("X")] for game in file]
    game = data[0]
    if game[1] == 1:
        selected = game[0]
    elif game[1] == 0:
        selected = (game[0]-1)%3
    elif game[1] == 2:
        selected = (game[0]+1)%2

    win_table = {0:[3,6,0],1:[0,3,6],2:[6,0,3]}
    
    score = sum([(strat[1] + 1 + win_table[strat[0]][strat[1]]) for strat in data])
    print(score)

    win_table2 = [0,3,6]
    coup = [[2,0,1],[0,1,2],[1,2,0]]

    score = sum([ ( coup[strat[0]][strat[1]] + 1 + win_table2[strat[1]] )  for strat in data])
    print(score)


