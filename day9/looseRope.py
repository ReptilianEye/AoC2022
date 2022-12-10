def calcMove(next, prev):
    vec = [next[0]-prev[0], next[1]-prev[1]]
    for i in range(2):
        if vec[i] % 2 == 0:
            vec[i] //= 2
    return tuple(vec)


def move_rope(rope, new_head):
    rope[0] = new_head
    for i in range(1, len(rope)):
        if max(abs(rope[i-1][0] - rope[i][0]), abs(rope[i-1][1] - rope[i][1])) >= 2:
            vec = calcMove(rope[i-1], rope[i])
            rope[i] = (rope[i][0] + vec[0], rope[i][1] + vec[1])
        else:
            break


def solve(dane, l=2):
    rope = [(0, 0)]*l
    visited = set()

    for line in dane:
        oper, times = line.strip().split(" ")
        match oper:
            case "U": step = (1, 0)
            case "D": step = (-1, 0)
            case "R": step = (0, 1)
            case "L": step = (0, -1)
        for _ in range(int(times)):
            move_rope(rope, (rope[0][0] + step[0], rope[0][1] + step[1]))
            visited.add(rope[-1])

    print(len(visited))


def looseRope():
    # file = "test.in"
    file = "dane.in"
    with open(file) as file:
        length = 2  # 10 for second star
        solve(file, length)


looseRope()
