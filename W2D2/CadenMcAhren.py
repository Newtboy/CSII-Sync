# your package is worth NOTHING. it serves ZERO purpose It should k-

# Import NOTHING

def main():
    numStudents = "Lorem Ipsum Dolor"
    while not numStudents.isdigit():
        numStudents = input("Total number of students: ")

    numStudents = int(numStudents)
    grades = []
    inp = ""
    while len(inp.split()) < numStudents:
        inp = input(f"Enter {numStudents} score(s): ")
    list = inp.split()
    max = 0
    for i in range(0, numStudents): # Cap loop at number of students
        item = int(list[i])
        if item > max:
            max = item
        grades.append(int(list[i]))
    sum = 0
    for i in range(0,len(grades)):
        printGrade(grades, max, i)
        sum += grades[i]
    sum /= numStudents

    print(f"The average score is {sum:0.2f}, a grade of {getGrade(sum, max)}")

def getGrade(score, max) -> str:
    if (score >= max-10):
        return "A"
    elif (score >= max-20):
        return "B"
    elif (score >= max-30):
        return "C"
    elif (score >= max-40):
        return "D"
    else:
        return "F"

def printGrade(gList, max, index):
    print(f"Student {index + 1} score is {gList[index]} and grade is {getGrade(gList[index], max)}")


if __name__ == "__main__":
    main()