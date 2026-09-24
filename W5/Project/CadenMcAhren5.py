# package null.wizard.newtboy

import csv
import io
import os
from os.path import isfile
import re


def main(): # {
    file = "" # my IDE would not shut up if I didn't add this
    while (True): # {
        try: # {
            fileName = input("Enter input filename: ").strip()
            fileName = fileName.strip()
            fileName = "files" + os.sep + fileName
            if (not isfile(fileName)): # {
                raise FileNotFoundError()
        # }
        except FileNotFoundError: # {
            print("File not found")
            continue
        # }
        break
    # }
    outStr = input("Output file name: ").strip()
    outStr = "files" + os.sep + outStr
    try: # {
        if (isfile(outStr)):  # {
            raise FileExistsError()
        # }
        pass
    # }
    except FileExistsError: # {
        inp = input("File exists. Overwrite? (y/n): ").lower()
        if (inp[0] == "n"): # {
            found = False
            i = 0
            while (not found): # {
                i += 1
                found = not isfile(f"{outStr[:-4]} ({i}).csv")
                pass
            # }
            outStr = f"{outStr[:-4]} ({i}).csv"
        # }
        else: # {
            outStr = f"{outStr}"
            pass
        # }
        pass
    # }

    emailRE = r"\S[a-z0-9A-Z\.]+@[\.A-Za-z0-9]+"

    with open(fileName, "r") as f: # {
        with open(outStr, "w", newline="") as csvF: # {
            csvW = csv.writer(csvF, delimiter=",")
            csvW.writerow(["Email", "Time","Confidence"])
            lines = f.readlines()
            email = None
            time = None
            confidence = None
            avg = 0.0
            numGroups = 0

            for i in range(0, len(lines)): # {
                if (re.search(r"^From: ", lines[i])): # {
                    email = re.search(emailRE, lines[i])
                # }
                elif(re.search("^X-DSPAM-Processed: ", lines[i])): # {
                    time = re.search(r"[0-9]+:[0-9]+:[0-9]+\S", lines[i])
                # }
                elif(re.search(r"X-DSPAM-Confidence: ", lines[i])): # {
                    confidence = re.search(r"0\.[0-9]*\S", lines[i])
                # }
                if ((email is not None and time is not None and confidence is not None)): # {
                    numGroups += 1
                    time = time.group(0)
                    if (time[0] == "0"): # {
                        time = time[1:]
                        pass
                    # }
                    csvW.writerow([email.group(0), time, confidence.group(0)])
                    avg += float(confidence.group(0))
                    email = None
                    time = None
                    confidence = None
                # }
            # }
            if (numGroups == 0): # {
                raise ZeroDivisionError("No Confidence values present!")
            avg = avg / numGroups
            csvW.writerow(["", "Average", f"{avg: 0.4f}"])
        # }
    # }
    print("Data stored!")
# }

if (__name__ == "__main__"): # {
    try: # {
        main()
        pass
    # }
    except ZeroDivisionError as e: # {
        print(e)
        pass
    # }
# }