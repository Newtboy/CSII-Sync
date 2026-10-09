import random

def mergeSort(ls: list[int]):
    if len(ls) <= 1:
        return ls

    mid = len(ls) // 2

    leftHalf = mergeSort(ls[:mid])
    rightHalf = mergeSort(ls[mid:])

    out = []

    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
        if leftHalf[leftIndex] < rightHalf[rightIndex]:
            out.append(leftHalf[leftIndex])
            leftIndex += 1
        else:
            out.append(rightHalf[rightIndex])
            rightIndex += 1

    out.extend(leftHalf[leftIndex:])
    out.extend(rightHalf[rightIndex:])

    return out
# }

def main():
    l = []

    for i in range(100):
        l.append(random.randint(-200, 200))

    l = mergeSort(l)
    print(l)


if __name__ == "__main__":
    main()