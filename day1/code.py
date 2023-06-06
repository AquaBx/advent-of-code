liste = []

with open("data.txt") as file:
    data = file.read()

    for lutin in data.split("\n\n"):
        sum = 0
        for item in lutin.split("\n"):
            sum+=int(item)
        liste.append(sum)

liste.sort()
print(liste[-3:])

print(67758+67958+74198)