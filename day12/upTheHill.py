
def solve(T):
    n = len(T)
    m = len(T[0])
    steps = ((1, 0), (0, 1), (-1, 0), (0, -1))  # steps which can be done
    inf = n*m+1  # inf > maximum steps
    distance = [[inf for _ in range(m)] for _ in range(n)]
    # finding poz of the start and the end
    start = end = None
    for w in range(len(T)):
        k_e = T[w].index('E') if 'E' in T[w] else None
        if k_e is not None:
            end = (w, k_e)
        k_s = T[w].index('S') if 'S' in T[w] else None
        if k_s is not None:
            start = (w, k_s)

        if start and end:
            break

    # I will record shortest path for every node
    distance[end[0]][end[1]] = 0
    # after saving position of start and end I set them to a and z
    T[end[0]][end[1]] = 'z'
    T[start[0]][start[1]] = 'a'
    # queue of nodes to work with
    q = [end]
    while len(q):
        pos = q.pop(0)
        for step in steps:
            next_p = (pos[0]+step[0], pos[1]+step[1])
            if 0 <= next_p[0] and next_p[0] < n and 0 <= next_p[1] and next_p[1] < m:
                if ord(T[pos[0]][pos[1]]) - ord(T[next_p[0]][next_p[1]]) <= 1 and distance[next_p[0]][next_p[1]] > distance[pos[0]][pos[1]]:
                    if (next_p[0], next_p[1]) not in q:
                        q.append((next_p[0], next_p[1]))
                    distance[next_p[0]][next_p[1]] = min(
                        distance[next_p[0]][next_p[1]], distance[pos[0]][pos[1]]+1)
    # looking for lowest amount of steps from 'a'
    min_s = inf
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 'a':
                min_s = min(min_s, distance[i][j])

    print(distance[start[0]][start[1]])   #output fs
    print(min_s)  # output ss


# file = "test.in"
file = "dane.in"
T = []
with open(file) as file:
    # reading files
    for line in file:
        line = line.strip()
        l = []
        for el in line:
            l.append(el)
        T.append(l)

    # solution
    solve(T)
