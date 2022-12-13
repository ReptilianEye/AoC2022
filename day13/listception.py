
from functools import cmp_to_key

#comparator funtion
def check_req(l1, l2):
    for i in range(len(l1)):
        if i >= len(l2):
            return -1

        left = l1[i]
        right = l2[i]
        if type(left) == int and type(right) == int:
            if left < right:
                return 1

            if left > right:
                return -1

        elif type(left) == list and type(right) == list:
            res = check_req(left, right)

            if res != 0:
                return res
        else:
            if type(left) == list:
                res = check_req(left, [right])
            else:
                res = check_req([left], right)
            if res != 0:
                return res

    if len(l1) == len(l2):
        return 0
    else:
        return 1


inf = 10**10


def readInput(l, i=0):
    sub_l = []
    i += 1
    while i < len(l) and l[i] != ']':
        if l[i] == '[':
            i, ans = readInput(l, i)
            sub_l.append(ans)

        elif l[i] != ",":
            dist1 = l.find(",", i+1)
            if dist1 == -1:
                dist1 = inf
            dist2 = l.find("]", i+1)
            if dist2 == -1:
                dist2 = inf

            el = l[i:min(dist1, dist2)]
            sub_l.append(int(el))
            i += len(el) - 1
        i += 1
    return i, sub_l


# file = "test.in"
file = "dane.in"
with open(file) as file:
    file = file.readlines()

# first star
s = 0
for l_i in range(0, len(file), 3):  # l_i = line iterator
    if check_req(readInput(file[l_i].strip())[1], readInput(file[l_i+1].strip())[1]) == 1:
        s += (l_i//3)+1
print(s)  # sol fs


# second star
T = []
for l_i in range(0, len(file), 3):  # l_i = line iterator
    T.append(readInput(file[l_i].strip())[1])
    T.append(readInput(file[l_i+1].strip())[1])
# driver packets 1 and 2
dp_1 = [[2]]
dp_2 = [[6]]

T.append(dp_1)
T.append(dp_2)
T.sort(key=cmp_to_key(check_req), reverse=True)
print((T.index(dp_1)+1)*(T.index(dp_2)+1))  # sol ss
