def read_input(file):
    map = []
    for line in file:
        l = [char for char in line]
        l.pop()  # removing \n
        if len(l) == 0:
            break
        map.append(l)
    instr_line = file.readline()
    instructions = []

    while len(instr_line):
        R_poz = instr_line.find("R")
        L_poz = instr_line.find("L")

        cut = min(R_poz, L_poz) if min(
            R_poz, L_poz) != -1 else max(R_poz, L_poz)
        if cut == -1:
            cut = len(instr_line)
        instr = instr_line[:cut]
        if instr == "":
            instructions.append(instr_line[0])
            instr_line = instr_line[1:]

        else:
            instructions.append(int(instr))
            instr_line = instr_line[cut:]

    return map, instructions


def overlap(dir, pos, T):
    match dir:
        case 0:
            i = pos[1]
            while i-1 >= 0 and T[pos[0]][i-1] != " ":
                i -= 1
            else:
                if T[pos[0]][i] == "#":
                    return pos
                else:
                    return (pos[0], i)

        case 1:
            i = pos[0]
            while i-1 >= 0 and T[i-1][pos[1]] != " ":
                i -= 1
            else:
                if T[i][pos[1]] == "#":
                    return pos
                else:
                    return (i, pos[1])
        case 2:
            i = pos[1]
            while i+1 < len(T[pos[0]]) and T[pos[0]][i+1] != " ":
                i += 1
            else:
                if T[pos[0]][i] == "#":
                    return pos
                else:
                    return (pos[0], i)
        case 3:
            i = pos[0]
            while i+1 < len(T) and pos[1] < len(T[i+1]) and T[i+1][pos[1]] != " ":
                i += 1
            else:
                if T[i][pos[1]] == "#":
                    return pos
                else:
                    return (i, pos[1])


directions = {0: ">", 1: "v", 2: "<", 3: "^"}


def move(pos, dir, steps, T):
    i = 0
    match dir:
        case 0:
            while i < steps:
                T[pos[0]][pos[1]+i] = directions[dir]
                if pos[1]+i+1 >= len(T[pos[0]]) or T[pos[0]][pos[1]+i+1] == " ":
                    res = overlap(dir, (pos[0], pos[1]+i), T)
                    if res == (pos[0], pos[1]+i):
                        break
                    else:
                        pos = res
                    steps -= i + 1
                    i = -1
                elif T[pos[0]][pos[1]+i+1] == "#":
                    break
                i += 1
            T[pos[0]][pos[1]+i] = directions[dir]
            return (pos[0], pos[1]+i)

        case 1:
            while i < steps:
                T[pos[0]+i][pos[1]] = directions[dir]

                if pos[0]+i+1 >= len(T) or pos[1] >= len(T[pos[0]+i+1]) or T[pos[0] + i+1][pos[1]] == " ":
                    res = overlap(dir, (pos[0]+i, pos[1]), T)
                    if res == (pos[0]+i, pos[1]):
                        break
                    else:
                        pos = res
                    steps -= i + 1
                    i = -1
                elif T[pos[0] + i+1][pos[1]] == "#":
                    break
                i += 1
            T[pos[0]+i][pos[1]] = directions[dir]
            return (pos[0]+i, pos[1])
        case 2:
            while i < steps:
                T[pos[0]][pos[1]-i] = directions[dir]

                if pos[1]-i-1 < 0 or T[pos[0]][pos[1]-i-1] == " ":
                    res = overlap(dir, (pos[0], pos[1]-i), T)
                    if res == (pos[0], pos[1]-i):
                        break
                    else:
                        pos = res
                    steps -= i + 1
                    i = -1
                elif T[pos[0]][pos[1]-i-1] == "#":
                    break
                i += 1
            T[pos[0]][pos[1]-i] = directions[dir]
            return (pos[0], pos[1]-i)
        case 3:
            while i < steps:
                T[pos[0]-i][pos[1]] = directions[dir]
                if pos[0]-i-1 < 0 or T[pos[0] - i-1][pos[1]] == " ":
                    res = overlap(dir, (pos[0] - i, pos[1]), T)
                    if res == (pos[0] - i, pos[1]):
                        break
                    else:
                        pos = res
                    steps -= i + 1
                    i = -1
                elif T[pos[0] - i-1][pos[1]] == "#":
                    break
                i += 1
            T[pos[0]-i][pos[1]] = directions[dir]
            return (pos[0]-i, pos[1])


def walk(instr, map):
    dir = 0
    poz = (0, map[0].index("."))
    for i in instr:
        if i == "L":
            dir = (dir+3) % 4
        elif i == "R":
            dir = (dir+1) % 4
        else:
            poz = move(poz, dir, i, map)
    return poz, dir


# file = "test.in"
file = "dane.in"
with open(file) as file:
    map, instr = read_input(file)
end = walk(instr, map)
result = (end[0][0]+1)*1000+(end[0][1]+1)*4+end[1]
print(result)