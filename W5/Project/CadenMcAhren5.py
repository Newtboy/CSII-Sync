# package null.wizard.newtboy

import csv
import os
from os.path import isfile
import re


def main(): # {
    fileName = "" # my IDE would not shut up if I didn't add this
    while (True): # {
        try: # {
            fileName = input("Enter input filename: ").strip()
            fileName = fileName.strip()
            fileName = "files" + os.sep + fileName
            f = open(fileName, "r") # force crash if not exist
        # }
        except FileNotFoundError: # {
            print("File not found")
            continue
        # }
        else: # {
            f.close() # If it works, close it
            break
        # }
    # }
    outStr = input("Output file name: ").strip()
    outStr = "files" + os.sep + outStr
    if (os.path.isfile(outStr)):  # {
        inp = input("File exists. Overwrite? (y/n): ").strip().lower()
        while (inp != "y" and inp != "n"): # {
            inp = input("File exists. Overwrite? (y/n): ").strip().lower()
        # }
        if (inp[0] == "n"):  # {
            inp1 = input("Enter file name: ")
            while (isfile("files" + os.sep + inp1)):  #
                print("File exists.")
                inp1 = input("Enter file name: ")
                continue
            # }
            outStr = "files" + os.sep + inp1
        # }
        elif (inp[0] == "y"):  # {
            outStr = f"{outStr}"
            pass
        # }
    # }

    emailRE = r"\S[a-z0-9A-Z\.]+@[\.A-Za-z0-9]+\S"

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
            csvW.writerow(["", "Average",f"{avg:.4f}"])
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