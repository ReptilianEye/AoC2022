def read(file):
    dane = {}
    for line in file:
        line = line.strip().split(":")
        val = int(line[1]) if len(line[1]) < 8 else line[1].strip().split(" ")
        dane[line[0]] = val
    return dane


def solve(dane):
    def solve_r(instr, dane):
        if type(instr) is int:
            return instr
        else:
            return eval(f"{solve_r(dane[instr[0]],dane)}{instr[1]}{solve_r(dane[instr[2]],dane)}")
    # return round(solve_r(dane["root"],dane))
    return (solve_r(dane[dane["root"][0]],dane)),(solve_r(dane[dane["root"][2]],dane))



# file = "test.in"
file = "dane.in"

with open(file) as file:
    dane = read(file)
# print(solve(dane))
i = 0
pow = 0
higher = False
while True:
    dane["humn"] = i
    res = solve(dane)
    print(res)
    if res[0] > res[1]:
        if not higher:
            pow = 0
        higher = True
        i += 2**pow
        pow += 1
    if res[0] < res[1]:
        if higher:
            pow = 0
        higher = False
        i -= 2**pow
        pow += 1
    if res[0] == res[1]:
        print(i)
        break
    i += 1