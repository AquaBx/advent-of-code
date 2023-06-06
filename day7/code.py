with open("day7/data.txt") as file:
    fread = file.read().replace("$ ls\n","").split("$ cd")
    dico = {"files":{"/":{"size":0,"files":{}}}}
    path = []
    files = [item.split("\n") for item in fread if  len(item) > 0]
    size = 0
    for item in files:
        if item[0].replace(" ","") == "..":
            path.pop()
        else:
            path.append(item[0].replace(" ",""))
            path_ref = dico

            for dir in path:
                path_ref = path_ref["files"][dir]

            for file in item[1:]:
                if file != "":
                    file = file.split()
                    if file[0] == "dir":                        
                        path_ref["files"][file[1].replace(".","_")] = {"size":0,"files":{}}
                    else :
                        path_ref["files"][file[1]] = int(file[0])
                        size += int(file[0])

                        path_ref2 = dico
                        for dir in path:
                            path_ref2 = path_ref2["files"][dir]
                            path_ref2["size"] += int(file[0])

    list_of_max = []
    list_to_filter = [ dico["files"] ]
    while len(list_to_filter) > 0 :
        filt = list_to_filter.pop() 
        for key in filt:
            try:
                a = filt[key]["files"]
                if filt[key]["size"] < 100000:
                    list_of_max.append(filt[key]["size"])
                list_to_filter.append( filt[key]["files"] )
            except:pass
        
    print(sum(list_of_max))


    list_of_max = []
    list_to_filter = [ dico["files"] ]
    while len(list_to_filter) > 0 :
        filt = list_to_filter.pop() 
        for key in filt:
            try:
                a = filt[key]["files"]
                if filt[key]["size"] >= dico["files"]["/"]["size"]-40000000:
                    list_of_max.append(filt[key]["size"])
                list_to_filter.append( filt[key]["files"] )
            except:pass
    
    print(min(list_of_max))