id = 0


class Node:

    def __init__(self, val) -> None:
        global id
        self.val = val
        self.id = id
        id += 1


def move(poz, T):
    el = T.pop(poz)
    poz = (poz + el.val) % len(T)
    if poz == 0:
        T.append(el)
    else:
        T.insert(poz, el)
    return T


def result(T):
    res = [el.val for el in T]
    return res[(res.index(0) + 1000) % len(res)] + res[(res.index(0) + 2000) %
                                                    len(res)] + res[(res.index(0) + 3000) % len(res)]



def solve(T, rounds):
    prime_poz = tuple(T)
    for _ in range(rounds):
        for el in prime_poz:
            i = 0
            while T[i].id != el.id:
                i += 1
            else:
                move(i, T)
    print(result(T))
    return T


# file = "test.in"
file = "dane.in"

# key = 1   # first star
key = 811589153  # sec star
with open(file) as file:
    T = [Node(int(line)*key) for line in file]

rounds = 10  # sec star
# rounds = 1 # first star

solve(T, rounds)
