monkeys = []


class Monkey():
    def __init__(self, items, inc_type, inc, div, t, f) -> None:
        self.items = items
        self.inc_type = inc_type
        self.inc = inc
        self.div = div
        self.test_true = t
        self.test_false = f

    def sim_operation(self):
        inc = self.items[0] if self.inc == "old" else int(self.inc)
        if self.inc_type == "*":
            self.items[0] *= inc
        else:
            self.items[0] += inc
        self.items[0] %= mod

    def bored(self):
        self.items[0] //= 3

    def test(self):
        item = self.items.pop(0)
        if item % self.div == 0:
            self.pass_to(self.test_true, item)
        else:
            self.pass_to(self.test_false, item)

    def pass_to(self, to, item):
        monkeys[to].items.append(item)


def solve(rounds=20):
    inspects = [0 for _ in range(len(monkeys))]
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            inspects[i] += len(monkey.items)
            for _ in range(len(monkey.items)):
                monkey.sim_operation()
                # monkey.bored()
                monkey.test()

    inspects.sort(reverse=True)
    print(inspects[0]*inspects[1])


# zbieram wartosc iloczynu wszystkich dzielników, ponieważ jeśli liczbę z pewną cechą podzielności
# zmoduluje takim iloczynem, to ona dalej będzie podzielna lub nie przez czynniki tego iliczynu
mod = 1


def inputData(file):
    i = 1
    while i < len(file):
        global mod
        monkey = {}
        items = []
        for el in file[i].strip().split()[2:]:
            items.append(int(el.replace(",", "")))
        monkey.update({"items": items})
        i += 1
        monkey.update({"inc_type": file[i].strip().split()[-2]})
        monkey.update({"inc": file[i].strip().split()[-1]})
        i += 1
        div = int(file[i].strip().split()[int(-1)])
        mod *= div
        monkey.update({"div": div})
        i += 1
        monkey.update({"t": int(file[i].strip().split()[-1])})
        i += 1
        monkey.update({"f": int(file[i].strip().split()[-1])})
        monkeys.append(
            Monkey(monkey["items"], monkey["inc_type"], monkey["inc"], monkey["div"], monkey["t"], monkey["f"]))
        i += 3


def getTheMonkey():
    # file = "dane.in"
    file = "test.in"
    with open(file) as file:
        file = file.readlines()
        inputData(file)
        dobrze = solve(10000)


getTheMonkey()
