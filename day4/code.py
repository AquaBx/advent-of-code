from this import d


def rangelist(liste):
    return range(int(liste[0]),int(liste[1])+1)

def is_contain(l1,l2):
    for item in l1:
        if item not in l2:
            return False
    return True

def overlap(l1,l2):
    for item in l1:
        if item in l2:
            return True
    return False

with open("data.txt") as file:
    fread = file.read().split("\n")
    data = [[rangelist(task.split("-")) for task in sack.split(",")] for sack in fread]
    
    contain = [(is_contain(item[0],item[1]) or is_contain(item[1],item[0])) for item in data] 
    overlap = [ overlap(item[0],item[1]) for item in data] 

    print(contain.count(True))
    print(overlap.count(True))

    