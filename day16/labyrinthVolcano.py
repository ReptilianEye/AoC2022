

nodes_num = {}


def read_input(file):
    valves_graph = {}
    rates = {}
    global nodes_num
    i = 0
    for line in file:
        line = line.strip()
        rate = int(line[line.find("=")+1:line.find(";")])
        valv = line[line.find("has")-4:line.find("has")-1].strip()
        nbors = [el.strip() for el in line[line.rfind("e")+2:].split(",")]
        nodes_num[valv] = i
        i += 1
        rates[valv] = rate
        valves_graph[valv] = nbors
    return valves_graph, rates


def normalize(graph):
    for node in graph:
        if rates[node] == 0:
            for nbor in graph[node]:
                graph[nbor] += graph[node]
                graph[nbor].remove(nbor)
    return graph
def count_distance(graph):
    inf = len(graph)+2
    dist_T = [[0 for _ in range(len(graph))]for _ in range(len(graph))]
    for node in graph:
        visited = [node]
        i = 0
        q = [(node, i)]
        while len(q) > 0:
            parent = q.pop(0)
            for nbor in graph[parent[0]]:
                if nbor not in visited:
                    visited.append(nbor)
                    dist_T[nodes_num[node]][nodes_num[nbor]] = parent[1] + 1
                    q.append((nbor, parent[1]+1))
    for line in dist_T:
        for el in line:
            print(el, end=" ")
        print()


def bfs_best(start, opened, Graph, rates, steps_left, szuk):
    visited = [start]
    q = [(0, 0, start)]
    best_val = (0, -10**10, "")
    steps = 0
    while len(q):
        parent = q.pop(0)
        for nbor in Graph[parent[2]]:
            if nbor not in visited:
                if nbor not in opened:
                    rate_in = rates[nbor] * (steps_left-parent[0] - 2)
                    # open_cost = 1
                    child = (parent[0] + 1, rate_in, nbor)
                    if child[2] == szuk:
                        return child
                    if best_val[1] < child[1]:
                        best_val = child
                else:
                    child = (parent[0]+1, 0, nbor)
                q.append(child)

        visited.append(child[2])
    return best_val


def get_into_tunnels(valves_graph, rates, time_left):
    # def get_into_tunnels_r(valv='AA', visited=(), time_left=30, score=0, step=0):
    #     if time_left == 0:
    #         return score, valv
    #     max_released = -1
    #     for nbor in valves_graph[valv]:
    #         inc = 0
    #         if nbor not in visited:
    #             node_max = max(get_into_tunnels_r(
    #                 nbor, visited+(valv), time_left-2, score + ), get_into_tunnels_r(nbor, visited+(valv), time_left-1, score))
    #             if max_released < released:
    #                 max_released = released
    #                 best_node = ""
    #     return max_released, best_node
    # print(get_into_tunnels_r())
    # print(get_into_tunnels_r("EE", ["DD"]))
    curr = "AA"
    visited_global = ["AA"]
    score = 0
    # l = ["DD", "BB", "JJ", "HH", "EE", "CC"]
    while time_left > 0:
        # for el in l:
        best_val = bfs_best(curr, visited_global,
                            valves_graph, rates, time_left)
        if best_val[2] == "":
            break
        score += best_val[1]
        time_left -= best_val[0]+1
        curr = best_val[2]
        visited_global.append(curr)
    print(score)


file = "test.in"
with open(file) as file:
    file = file.readlines()
valves_graph, rates = read_input(file)
count_distance(valves_graph)
print(nodes_num)
get_into_tunnels(valves_graph, rates, 30)
