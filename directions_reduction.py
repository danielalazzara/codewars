def dirReduc(arr):
    opposite = {
        "NORTH":"SOUTH",
        "SOUTH":"NORTH",
        "EAST":"WEST",
        "WEST":"EAST",
    }
    dir = []
    for i in arr:
        if len(dir) == 0 or dir[-1] != opposite[i]:
            dir.append(i)
            continue
        dir.pop()
    return dir
        
