# package null.wizard.newtboy

import statistics as stats

def divide(vals): # {
    z = vals[0]
    for num in vals[1:]: # {
        if (num == 0): # {
            raise ZeroDivisionError("List contains a 0")
            pass
        # }
        z = z / num
        pass
    # }
    return z

def valUser(): # {
    num = input("Enter number (q to exit): ")
    ls = []
    while (num != "q"):  # {
        try:  # {
            num = int(num)
            ls.append(num)
        except ValueError:  # {
            print("Not an int")
            pass
        # }
        num = input("Enter val, q to exit: ")
    # }
    print(f"Sum of vals is {sum(ls)}")
    print(f"Div of vals is {divide(ls)}")
# }

def valUser2(): # {
    inp = input("Enter number (e to exit)")
    ls = []
    while (inp[0] != "e"):  # {
        if (not inp.isdigit()):  # {
            raise ValueError("Non-digit entered")
        # }
        ls += inp
        inp = input("Enter number (e to exit)")
        pass
    # }

# }

def main(): # {
    valUser()
# }

if (__name__ == "__main__"): # {
    main()
    pass
# }