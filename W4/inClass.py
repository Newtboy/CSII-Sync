import csv
from datetime import datetime as dt


def main(): # {
    formats = "%H:%M"
    with open("flights.csv", "r") as f: # {
        with open("flightLengths.csv", "w", newline="") as fL: # {
            reader = csv.reader(f);
            writer = csv.writer(fL);

            first = True
            for row in reader: # {
                if (first): # {
                    first = False;
                    writer.writerow(row[:-1] +["Flight Length"] + [row[-1]]);
                    continue
                    pass
                # }
                arrTime = row[4];
                depTime = row[3];
                tDelta = dt.strptime(arrTime, formats)-dt.strptime(depTime, formats)
                writer.writerow(row[:-1] + [tDelta] + [row[-1]])
                pass
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
