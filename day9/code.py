def affiche_grid(rope_points):
    grid = [["." for _ in range(1000)] for _ in range(1000)]
    for i in range(len(rope_points)-1,-1,-1):
    
        ni = rope_points[i]["position"]["i"]
        nj = rope_points[i]["position"]["j"]
        
        grid[ni][nj] = str(i)

    for item in grid:
        print(item)
    print()

def move_head(direction,H):
    if direction == "R":
        H["position"]["j"] += 1
    elif direction == "L":
        H["position"]["j"] -= 1
    elif direction == "U":
        H["position"]["i"] -= 1
    elif direction == "D":
        H["position"]["i"] += 1

def move_tail(H,T):
    if (H["position"]["i"] - T["position"]["i"])**2==4:
        if (H["position"]["j"] - T["position"]["j"])**2 == 1:
            T["position"]["j"] = H["position"]["j"]
        elif (H["position"]["j"] - T["position"]["j"])**2 == 4:
            T["position"]["j"] = int ( (H["position"]["j"] + T["position"]["j"])/2 )
        T["position"]["i"] = int( (H["position"]["i"] + T["position"]["i"])/2 )

    elif (H["position"]["j"] - T["position"]["j"])**2==4:
        if (H["position"]["i"] - T["position"]["i"])**2 == 1:
            T["position"]["i"] = H["position"]["i"]
        elif (H["position"]["i"] - T["position"]["i"])**2 == 4:
            T["position"]["i"] = int( (H["position"]["i"] + T["position"]["i"])/2 )

        T["position"]["j"] = int ( (H["position"]["j"] + T["position"]["j"])/2 )

def filter(list):
    nlist = []
    for item in list:
        if item not in nlist:
            nlist.append(item)
    return nlist

with open("./day9/message.txt") as file:
    fread = file.read().split("\n")

    rope_points = [ {"position":{"i":5,"j":0}} for _ in range(10)]

    T_pos = set()
    T_pos.add((rope_points[-1]["position"]["i"],rope_points[-1]["position"]["j"]))

    for move in fread:
        move = move.split(" ")
        direction = move[0]
        distance = int(move[1])

        for i in range(distance):
            move_head(direction,rope_points[0])
            for j in range(1,len(rope_points)):
                move_tail(rope_points[j-1], rope_points[j])
            T_pos.add((rope_points[-1]["position"]["i"],rope_points[-1]["position"]["j"]))
            print(rope_points)
            # affiche_grid(rope_points)
    print(len(T_pos))