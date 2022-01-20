with open("input.txt") as txt:
    lines = txt.readlines()
    total = 0
    ints = []
    for line in lines:
        ints.append(int(line.strip()))
    sums = []
    for i in range(2, len(ints)):
        sums.append(ints[i-2]+ints[i-1]+ints[i])
    for i in range(len(sums)):
        if sums[i] > sums[i-1]:
            total += 1
    print(total)
