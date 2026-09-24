# package null.wizard.newtboy

import csv
import os
from os.path import isfile
import re


def main(): # {
    while (True): # {
        try: # {
            fileName = input("Enter input filename: ")
            file = open("files" + os.sep + fileName)
        # }
        except FileNotFoundError: # {
            print("File not found")
            continue
        # }
        break
    # }

    fileN = file.name
    file.close()
    try: # {
        if (isfile("files" + os.sep + "output.csv")):  # {
            raise FileExistsError()
        # }
        pass
    # }
    except FileExistsError: # {
        outStr = "output.csv"
        inp = input("File exists. Overwrite? (y/n): ")
        if (inp[0] == "n"): # {
            found = False
            i = 0
            while (not found): # {
                i += 1
                found = not isfile(f"output ({i}).csv")
                pass
            # }
            outStr = f"output ({i}).csv"
        # }
        else: # {
            # Just in case
            outStr = "output.csv"
            pass
        # }
        pass
    # }
    else: # {
        # Just in case (and so ide shuts up), first creation
        outStr = "output.csv"
        pass
    # }
    emailRE = r"\S[a-z0-9A-Z\.]+@[\.A-Za-z0-9]+"
    csvRE = r".*[0-9]\S$"
    with open(fileN, "r") as f: # {
        with open("files" + os.sep + outStr, "w", encoding=",") as csvF: # {
            csvW = csv.writer(csvF)
            csvW.writerow(["Email", "Time","Confidence"])
            for line in f.readlines(): # {
                if (re.search("^From: ", line)): # {

        # }
    # }
# }

if (__name__ == "__main__"): # {
    main()
    pass
# }