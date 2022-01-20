with open("input2.txt") as txt:
    lines = txt.readlines()
    nlines = []
    horizon = 0
    depth = 0
    aim = 0
    for line in lines:
        nlines.append(line.strip())
    print(nlines)
    for line in nlines:
        direction, num = line.split(" ")
        if direction == "forward":
            horizon += int(num)
            depth += aim * int(num)
        elif direction == "down":
            aim += int(num)
        elif direction == "up":
            aim -= int(num)
        else:
            print(direction)
    print(horizon, depth)
    print(horizon * depth)
