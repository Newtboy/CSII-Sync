#help I need mental space to assume package and imports*

# sudo import

def vote_menu() -> str:
    print("----------------------------------")
    print("VOTE MENU\n----------------------------------")
    print("v: Vote\nx: Exit")
    inp = input("Option: ").lower().strip()
    while inp != "v" and inp != "x":
        inp = input("Invalid (v/x): ").strip().lower()

    return inp

def candidate_menu() -> int:
    c1 = "Laurent"
    c2 = "Kwasi"
    c3 = "Jessica"
    print("----------------------------------")
    print("CANDIDATE MENU")
    print("----------------------------------")
    print(f"1: {c1}")
    print(f"2: {c2}")
    print(f"3: {c3}")
    inpStr = input("Candidate: ").strip()

    while inpStr != "1" and inpStr != "2" and inpStr != "3":
        inpStr = input("Invalid (1/2/3): ").strip()
    return int(inpStr)

def main():
    c1Votes = 0
    c2Votes = 0
    c3Votes = 0

    while (vote_menu() != "x"):
        cand = candidate_menu()
        if cand == 1:
            print("Voted Laurent")
            c1Votes += 1
        if cand == 2:
            print("Voted Kwasi")
            c2Votes += 1
        if cand == 3:
            print("Voted Jessica")
            c3Votes += 1

    print("-------------------------------------------------------")
    print(f"Laurent – {c1Votes}, Kwasi – {c2Votes}, Jessica – {c3Votes}, ", end="")
    print(f"Total – {c1Votes + c2Votes + c3Votes}")
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main()