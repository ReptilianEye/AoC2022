def count_nbors(new, placed):
    s = 0
    for c in placed:
        if abs(c[0]-new[0]) + abs(c[1]-new[1]) + abs(c[2]-new[2]) == 1:
            s += 1
    return s


# file = "test.in"
file = "dane.in"

with open(file) as file:
    s = 0
    placed = []
    for line in file:
        line = line.strip().split(",")
        poz = tuple(int(el) for el in line)
        s += 6-count_nbors(poz, placed)*2
        placed.append(poz)
print(s)
