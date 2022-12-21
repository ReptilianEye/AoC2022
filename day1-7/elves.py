import re
from math import ceil


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
            if min(pair[1]) <= max(pair[0]) <= max(pair[1]) or min(pair[1]) <= min(pair[0]) <= max(pair[1]) or min(pair[0]) <= max(pair[1]) <= max(pair[0]) or min(pair[0]) <= min(pair[1]) <= max(pair[0]):
                s += 1
                print(pair)
        print(s)

    # file = "dane/test4.in"
    file = "dane/dane4.in"
    with open(file) as file:
        # first_star(file)
        sec_star(file)


# dayFour()


def dayFive():
    class crateMover():
        def __init__(self, n=3):
            self.stack = [[] for _ in range(n)]
            self.size = n

        def add(self, el, _to):
            if 0 <= _to and _to < self.size:
                self.stack[_to].append(el)

        def move(self, _from, _to):
            self.stack[_to].append(self.stack[_from].pop())

        def move_many_block(self, n, _from, _to):

            self.stack[_to] += self.stack[_from][-n:]
            self.stack[_from] = self.stack[_from][:len(self.stack[_from])-n]

        def move_many_stack(self, n,  _from, _to):
            if n <= len(self.stack[_from]):
                for _ in range(n):
                    self.move(_from, _to)

        def _get_top(self, i):
            if len(self.stack[i]) == 0:
                return ""
            else:
                return self.stack[i][-1]

        def get_tops(self):
            return "".join([self._get_top(i) for i in range(self.size)])

    def first_and_sec_star(file):
        file = file.readlines()
        l = []
        d_w = 0
        while True:
            line = file[d_w]
            d_w += 1
            if "1" in line.strip():
                break

            j = 0
            temp = []
            while j < len(line):
                temp.append(line[j+1:j+2])
                j += 4
            l.append(temp)
        d_w += 1
        c = crateMover(len(l[-1]))

        for i in range(len(l)-1, -1, -1):
            for j in range(c.size):
                if l[i][j].strip() != "":
                    c.add(l[i][j], j)
        while d_w < len(file):
            line = file[d_w]
            instr = line.strip().split()
            # c.move_many_stack(int(instr[1]), int(instr[3])-1, int(instr[5])-1)
            c.move_many_block(int(instr[1]), int(instr[3])-1, int(instr[5])-1)

            # print(s.get_tops())
            d_w += 1
        print(c.get_tops())

    def sec_star(file):
        pass
    # file = "dane/test5.in"
    file = "dane/dane5.in"
    with open(file) as file:
        first_and_sec_star(file)

        # sec_star(file)
# dayFive()


def daySix():

    def check_dup(s):
        return len(s) == len(set(list(s)))

    def first__and_sec_star(line, l=4):
        i = 0
        while i+l < len(line):
            if check_dup(line[i:i+l]):
                print(i+l)
                return
            i += 1

    def sec_star(file):
        pass
    # file = "dane/test6.in"
    file = "dane/dane6.in"
    with open(file) as file:
        for line in file:
            first__and_sec_star(line.strip(), l=14)

        # sec_star(file)
# daySix()


def daySeven():
    import re
    into_dir = "\$ cd [a-z]"
    up_dir = "\$ cd \.\."
    ls = "\$ ls"
    command = "\$ [a-z]+"
    dir = "dir*"
    num = "[0-9]+"

    def sum_dir(file):
        nonlocal i
        i += 1
        s = 0
        n = len(file)
        while i < n and not re.search(command, file[i]):
            if not re.search(dir, file[i]):
                s += int(re.findall(num, file[i])[0])
            i += 1
        i -= 1
        return s

    def calc_size_fs(max_s, file):
        nonlocal i, sum
        n = len(file)
        s = 0
        while i < n and not re.search(up_dir, file[i]):
            if re.search(into_dir, file[i]):
                i += 1
                s += calc_size_fs(max_s, file)
                if i >= n:
                    return s
            if re.search(ls, file[i]):
                s += sum_dir(file)

            i += 1
        if s <= max_s:
            sum += s
        return s

    def calc_size_ss(min_s, file):
        nonlocal i
        n = len(file)
        s = 0
        while i < n and not re.search(up_dir, file[i]):
            if re.search(into_dir, file[i]):
                i += 1
                s += calc_size_ss(min_s, file)
                if i >= n:
                    return s
            if re.search(ls, file[i]):
                s += sum_dir(file)

            i += 1
        if s >= min_s:
            to_delete.append(s)
        return s
    # file = "dane/test7.in"
    file = "dane/dane7.in"
    with open(file) as file:
        filelines = file.readlines()
        file = [filelines[i].strip() for i in range(len(filelines))]
    i = 0
    sum = 0
    sys_size = calc_size_fs(100000, file)
    # print(sum)

    free_space = 70000000 - sys_size
    if free_space < 30000000:
        to_free = 30000000-free_space
    to_delete = [sys_size]
    i = 0
    calc_size_ss(to_free, file)
    print(min(to_delete))


daySeven()
