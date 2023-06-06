import math

def exec(old,string):
    if "*" in string:
        liste = [ (old if item=="old" else int(item)) for item in string.split("*")]
        if liste[0]==liste[1]:
            return (liste[0]*liste[1])%(23*19*17*13*11*7*5*3*2)
        return (liste[0]*liste[1])
    elif "-" in string:
        liste = [ (old if item=="old" else int(item)) for item in string.split("-")]
        return ( liste[0]-liste[1] )
    elif "+" in string:
        liste = [ (old if item=="old" else int(item)) for item in string.split("+")]
        return (liste[0]+liste[1])
    


def condition(val,cond):
    key = int(cond.split("by")[1].replace(" ",""))
    if val%key == 0:
        return True
    else:
        return False

nb_premier = []
for i in range (2,5000):
    prem = True
    for j in range(2,i//2+1):
        if i%j == 0:
            prem = False
    if prem:
        nb_premier.append(i)


def to_simple(i):
    init = i
    prod = []
    for j in nb_premier:
        if i%j == 0:
            i = i//j
            prod.append(j)
    if len(prod) == 0:
        return init
    else:
        p = 1
        for item in prod:
            p*=item
        return p


with open("./day11/data.txt") as file:
    fread = file.read().split("\n\n")

    dict = {}

    for item in fread:
        id = item.split("\n")[0].split(":")[0].lower()
        items = [ int(s) for s in item.split("\n")[1].split(":")[1].replace(" ","").split(",") ]
        new = item.split("\n")[2].split(":")[1].split("=")[1].replace(" ","")
        cond = item.split("\n")[3].split(":")[1]
        cond_true = item.split("\n")[4].split(":")[1].split("to ")[1]
        cond_false = item.split("\n")[5].split(":")[1].split("to ")[1]
        dict[id] = {"items":items,"new":new,"cond":cond,"true":cond_true,"false":cond_false,"count":0}

    for i in range(1,10001):
        for key in dict:
            for item in dict[key]["items"]:
                new = exec(item,dict[key]["new"])
                simple = new
                cond = condition(new, dict[key]["cond"])
                if cond:
                    end = dict[key]["true"]
                else:    
                    end = dict[key]["false"]
                dict[end]["items"].append(simple)
                dict[key]["count"] += 1

            dict[key]["items"] = []
        if i in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
            print(i,[dict[key]["count"] for key in dict])


