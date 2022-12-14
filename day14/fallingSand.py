
def readRocks(file):
    rocks_poz = []
    for line in file:
        rocks_poz.append(list((int(
            point[point.find(",")+1:]), int(point[:point.find(",")])) for point in line.strip().split(" -> ")))
    return rocks_poz


def fillWithRocks(Cave, from_, to_):
    curr = (from_[0], from_[1] % min_col+1)
    to_ = (to_[0], to_[1] % min_col+1)
    diff = (to_[0] - curr[0], to_[1] - curr[1])
    while diff != (0, 0):
        Cave[curr[0]][curr[1]+len(Cave[0])//2 - sand_dozer_poz[1]] = "#"
        diff = (to_[0] - curr[0], to_[1] - curr[1])
        curr = (curr[0] + (diff[0]//abs(diff[0]) if diff[0] != 0 else 0),
                (curr[1] + (diff[1]//abs(diff[1]) if diff[1] != 0 else 0)))


def placeRocks(r, c, rocks_poz):
    Cave = [["." for _ in range(c)] for _ in range(r)]
    for poz in rocks_poz:
        prev = ()
        for rock in poz:
            if prev:
                fillWithRocks(Cave, prev, rock)
            prev = rock
    return Cave


def sand(r, c, C):

    # if r+1 == len(C):
    # return False
    if C[r+1][c] == ".":
        return sand(r+1, c, C)
    if c-1 >= 0 and C[r+1][c-1] == ".":
        return sand(r+1, c-1, C)
    if c+1 < len(C[r]) and C[r+1][c+1] == ".":
        return sand(r+1, c+1, C)
    else:
        C[r][c] = "O"
        return (r, c)


def simulSand(Cave):
    i = 1
    global sand_dozer_poz
    sand_dozer_poz = (sand_dozer_poz[0], len(Cave[0])//2 + 1)
    while sand(sand_dozer_poz[0], sand_dozer_poz[1], Cave) != sand_dozer_poz:
        i += 1
    print(i)


# file = "test.in"
file = "dane.in"
with open(file) as file:
    file = file.readlines()
rocks_poz = readRocks(file)
rows = cols = -1
min_col = 10**10
for poz in rocks_poz:
    for rock in poz:
        min_col = min(min_col, rock[1])
        cols = max(cols, rock[1])
        rows = max(rows, rock[0])
for poz in rocks_poz:
    for i in range(len(poz)):
        poz[i] = (poz[i][0], poz[i][1] % min_col)
rows += 2
cols = cols % min_col + rows**2
sand_dozer_poz = (0, 500 % min_col)
Cave = placeRocks(rows, cols, rocks_poz)
Cave.append(["#" for _ in range(len(Cave[0]))])
simulSand(Cave)
