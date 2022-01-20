with open("input3.txt") as txt:
    lines = txt.readlines()
    nlines = []
    for line in lines:
        nlines.append((line.strip()))
    print(nlines)
    bits = [0 for i in range(len(nlines[0]))]
    print(bits)
    for i in nlines:
        for index, bit in enumerate(i):
            bits[index] += int(bit)
    print(bits)
    gamma = ""
    epsilon = ""
    for i in bits:
        if i < 500:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    print(int(gamma, 2) * int(epsilon, 2))
    print(len(nlines))