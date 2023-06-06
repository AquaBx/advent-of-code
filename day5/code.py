with open("day5/data.txt") as file:
    fread = file.read().split("\n\n")
    part1 = fread[0].split("\n")
    part2 = fread[1].split("\n")

    liste1 = []

    for i in range(len(part1)):
        line = part1[i]
        part1[i] = [x.replace("[","").replace("]","") for x in line.replace("    ", " ").split(" ")]

    liste1 = [[] for x in part1[-1] if x != '']
    for i in range(len(part1)-2,-1,-1):
        for j in range(len(part1[0])):
            if part1[i][j]!="":
                liste1[j].append(part1[i][j])
    
    instruction = [[int(y) for y in x.split(" ") if y not in ["move","from","to"]] for x in part2]
    # for inst in instruction:
    #     for i in range(inst[0]):
    #         liste1[inst[2]-1].append(liste1[inst[1]-1].pop())

    for inst in instruction:
        listt=[]
        for i in range(inst[0]):
            listt.append(liste1[inst[1]-1].pop())
        listt.reverse()
        for it in listt:
            liste1[inst[2]-1].append(it)
    print( "".join([x[-1] for x in liste1]) )