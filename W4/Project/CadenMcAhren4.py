# package null.wizard.newtboy

import os
import csv
import re

def main(): # {
    emailRE = r"\S[a-z0-9A-Z\.]+@[\.A-Za-z0-9]+"
    sumDict = dict()
    dictSum = 0
    inp = input("Do you care if time starts with 09? (y/n): ").lower()

    csvRE =  r".*[0-9]\S$"

    with open("input.txt", "r") as inpf: # {
        with open("output.csv", "w", newline="") as outCSV: # {
            with open("output.txt", "w") as outTXT: # {
                writer = csv.writer(outCSV)
                writer.writerow(["Email","Day","Date","Month","Year","Time"])
                outTXT.write(f"{"Email":40s} - Count\n")

                for line in inpf.readlines(): # {
                    found = re.search("From ", line)
                    if (found): # {
                        data = re.findall(emailRE + csvRE, line)
                        med = data[0].split()
                        if (med[4][0] == "0" and inp == "y"): # {
                            med[4] = med[4][1:]
                        # }
                        eddmyt = [med[0], med[1], med[3], med[2], med[5], med[4]]
                        writer.writerow(eddmyt)
                        pass
                    # }

                    # 2B
                    found = re.search("From:", line)
                    if (found): # { something exists
                        email = re.search(emailRE, line).group()
                        if (email not in sumDict): # {
                            sumDict[email] = 0
                            pass
                        # }
                        sumDict[email] += 1;
                        dictSum += 1;
                        pass
                    # }
                # }
                for email, num in sumDict.items(): # {
                    outTXT.write(f"{f"{email}":40s} - {num}\n")
                    pass
                # }
                outTXT.write("-"*49+"\n")
                outTXT.write(f"{"Total Emails":40s} - {dictSum}")
            # }
            pass
        # }
        pass
    # }
    pass
# }

if (__name__ == "__main__"): # {
    main();
    pass
# }