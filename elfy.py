def dayOne():
    top3 = [0, 0, 0]
    with open("dane/test1.in") as file:
        s = 0
        for line in file:
            line = line.strip()
            if line == "":
                top3[top3.index(min(top3))] = max(min(top3), s)
                s = 0
            else:
                s += int(line)
        top3[top3.index(min(top3))] = max(min(top3), s)
        print(top3)
        print(sum(top3))
# dayOne()


def dayTwo():
    def calc_score(round):
        opp = abs(ord("A") - ord(round[0]))+1
        me = abs(ord("X") - ord(round[1]))+1
        if me == opp:
            return 3 + me
        if opp-me in [-1, 2]:
            return 6+me
        else:
            return me

    def first_star(file):
        s = 0
        answ = {}
        for round in file:
            round = "".join(round.strip().split())
            if not answ.get(round, False):
                answ[round] = calc_score(round)
            s += answ[round]
        print(s)

    def sec_star(file):
        s = 0
        for line in file:
            round = line.strip().split()
            s += calc_score([round[0], chr(
                ord("X") + (ord(round[0])-ord("A")+ord(round[1])-ord("Y")) % 3)])
        print(s)
    with open("dane/dane2.in") as file:
        # first_star(file)
        sec_star(file)


# dayTwo()

def dayThree():
    def priority(item):
        if item == item.upper():
            return 27 + ord(item) - ord("A")
        else:
            return 1 + ord(item) - ord("a")

    def first_star(file):
        s = 0
        for line in file:
            line = line.strip()
            rucksacks = [line[:len(line)//2], line[len(line)//2:]]
            common = " "
            for item in rucksacks[0]:
                if item in rucksacks[1]:
                    common = item
                    break
            s += priority(common)
            # print(common)

        print(s)

    def sec_star(file):
        group = []
        s = 0
        for line in file:
            group.append(line.strip())

            if len(group) % 3 == 0:
                for item in group[0]:
                    if item in group[1] and item in group[2]:
                        common = item
                        break
                # print(common)
                s += priority(common)
                group = []
        print(s)

    # file = "dane/test3.in"
    file = "dane/dane3.in"
    with open(file) as file:
        # first_star(file)
        sec_star(file)


# dayThree()


def dayFour():
    def first_star(file):
        s = 0
        for line in file:
            pair = line.strip().split(",")
            for i in range(2):
                pair[i] = pair[i].split("-")
                pair[i] = [int(pair[i][0]), int(pair[i][1])]
            if max(pair[0]) >= max(pair[1]) and min(pair[0]) <= min(pair[1]) or max(pair[0]) <= max(pair[1]) and min(pair[0]) >= min(pair[1]):
                s += 1
                # print(pair)
        print(s)

    def sec_star(file):
        s = 0
        s = 0
        for line in file:
            pair = line.strip().split(",")
            for i in range(2):
                pair[i] = pair[i].split("-")
                pair[i] = [int(pair[i][0]), int(pair[i][1])]
            gora1 = max(pair[0])
            dol1 = min(pair[0])
            gora2 = max(pair[1])
            dol2 = min(pair[1])

            if dol2 <= gora1 <= gora2 or dol2 <= dol1 <= gora2 or dol1 <= gora2 <= gora1 or dol1 <= dol2 <= gora1:
                s += 1
                print(pair)
        print(s)

    # file = "dane/test4.in"
    file = "dane/dane4.in"
    with open(file) as file:
        # first_star(file)
        sec_star(file)


dayFour()
