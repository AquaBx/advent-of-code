def output(l1, l2) :
    return [ x for x in set(l1) if x in l2 ]
    # return [l1, l2, [ x for x in set(l1) if x in l2 ]]

def sum_prio(liste):
    sum=0
    for c in liste:
        car = c[0]
        if ord("A") <= ord(car) <= ord("Z"):
            sum+= ord(car)-ord("A")+27
        elif ord("a") <= ord(car) <= ord("z"):
            sum += ord(car)-ord("a")+1
    return sum

with open("data.txt") as file:
    fread = file.read().split("\n")
    data = [output(sack[:int(len(sack)/2)] , sack[int(len(sack)/2):]) for sack in fread]
    print(sum_prio(data))

    data2 = [output(output(fread[i],fread[i+1]),fread[i+2]) for i in range(0, len(fread),3 )]
    print(sum_prio(data2))