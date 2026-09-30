def first(old_list): # {
    nList = []
    for i in range(0,len(old_list)): # {
        nList.append(old_list[i] ** 2)
    # }
    return nList
# }
# O(n)
import re

def second(): # {
    lineWC = 0
    totWhC = 0
    sLineWC = []

    with open("f.txt", "r") as f: # {
        lines = f.readlines() # read() is technically faster but this seems stable for longer
        for i in range(0, len(lines)): # {
            lineWC += len(re.findall(r"\s", lines[i]))
            totWhC += lineWC
            sLineWC.append(lineWC)

def third(ints: list[list[int]]): # {
    for item in ints: # {
        for subItem in item: # {
            if (subItem < 0): # {
                return False
            # }
        # }
    # }
    return True
# }
