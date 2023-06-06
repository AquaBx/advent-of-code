def are_diff(list):
    for item in list:
        if list.count(item) > 1:
            return False
    return True

with open("day6/data.txt") as file:
    fread = file.read().split("\n")[0]
    i=0
    car = 14
    while not are_diff( fread[i:i+car] ):
        i+=1
    print(fread[i:i+car],i+car)
    