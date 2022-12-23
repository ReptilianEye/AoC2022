import numpy as np


def read_input(file):
    return np.array([[0 if el == "." else 1 for el in line.strip()] for line in file])


def extend_grove(Grove):
    if np.any(Grove[0, :]):
        Grove = np.r_[np.zeros((1, len(Grove[0])), np.int8), Grove]
    if np.any(Grove[-1, :]):
        Grove = np.r_[Grove, np.zeros((1, len(Grove[0])), np.int8)]
    if np.any(Grove[:, 0]):
        Grove = np.c_[np.zeros(len(Grove), np.int8), Grove]
    if np.any(Grove[:, -1]):
        Grove = np.c_[Grove, np.zeros(len(Grove), np.int8)]
    return Grove


def shrink_grove(Grove):
    while not np.any(Grove[0, :]):
        Grove = np.delete(Grove, 0, 0)
    while not np.any(Grove[-1, :]):
        Grove = np.delete(Grove, -1, 0)
    while not np.any(Grove[:, 0]):
        Grove = np.delete(Grove, 0, 1)
    while not np.any(Grove[:, -1]):
        Grove = np.delete(Grove, -1, 1)
    return Grove


def look_for_nbor(poz, Grove):
    return Grove[poz[0], poz[1]+1] in [1, -1] or Grove[poz[0]+1, poz[1]+1] in [1, -1] or Grove[poz[0]+1, poz[1]] in [1, -1] or Grove[poz[0]+1, poz[1]-1] in [1, -1] or Grove[poz[0], poz[1]-1] in [1, -1] or Grove[poz[0]-1, poz[1]-1] in [1, -1] or Grove[poz[0]-1, poz[1]] in [1, -1] or Grove[poz[0]-1, poz[1]+1] in [1, -1]


def make_proposition(poz, destinations, Grove):
    i, j = poz
    if look_for_nbor(poz, Grove):
        for dest in destinations:
            if dest == 0:
                east = (Grove[i, j+1], Grove[i-1, j+1], Grove[i+1, j+1])
                if 1 not in east and -1 not in east:
                    return (i, j+1)
            elif dest == 1:
                south = (Grove[i+1, j], Grove[i+1, j-1], Grove[i+1, j+1])
                if 1 not in south and -1 not in south:
                    return (i+1, j)

            elif dest == 2:
                west = (Grove[i, j-1], Grove[i-1, j-1], Grove[i+1, j-1])
                if 1 not in west and -1 not in west:
                    return (i, j-1)
            elif dest == 3:
                north = (Grove[i-1, j], Grove[i-1, j-1], Grove[i-1, j+1])
                if 1 not in north and -1 not in north:
                    return (i-1, j)
    return poz


def move_elves(Grove, propositions):
    Grove = np.zeros(np.shape(Grove), np.int8)
    for propo in propositions.keys():
        if len(propositions[propo]) == 1:
            Grove[propo] = 1
        else:
            for prev in propositions[propo]:
                Grove[prev] = 1
    return Grove


def check_of_the_same(propositions):
    for p in propositions:
        if len(propositions[p]) > 1:
            return False
        else:
            if p != propositions[p][0]:
                return False
    return True


def moving_elves(Grove, rounds=10**10):
    Grove = extend_grove(Grove)
    destinations = [3, 1, 2, 0]  # north, south, west, east
    for round in range(rounds):
        propositions = {}
        for i in range(len(Grove)):
            for j in range(len(Grove[i])):
                poz = (i, j)
                if Grove[poz] == 1:
                    propo = make_proposition((i, j), destinations, Grove)
                    res = propositions.get(propo, [])
                    propositions[propo] = res + [poz]
        if check_of_the_same(propositions):
            print(round+1)
            return
        destinations.append(destinations.pop(0))
        Grove = move_elves(Grove, propositions)
        Grove = extend_grove(Grove)
    Grove = shrink_grove(Grove)
    print(np.count_nonzero(Grove == 0))


# file = "test.in"
file = "dane.in"
with open(file) as file:
    # moving_elves(read_input(file),10) #first star
    moving_elves(read_input(file)) #second star
