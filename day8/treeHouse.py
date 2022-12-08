import numpy


def treeHouse():
    def eval(T, w, k):
        me = T[w, k]
        right = T[w, k+1:]
        left = numpy.flip(T[w, :k], 0)
        down = T[w+1:, k]
        up = numpy.flip(T[:w, k], 0)
        # fs
        # return me > max(right) or me > max(left) or me > max(down) or me > max(up)

        # ss
        return how_many_seen(me, right) * how_many_seen(me, left) * how_many_seen(me, down) * how_many_seen(me, up)

    def how_many_seen(me, trees):  # ss
        s = 0
        for t in trees:
            s += 1
            if t >= me:
                break
        return s

    def visible(T):
        n = len(T)
        best_scenic = -1  # second star
        # s = 4*(n-1)   #first star
        for i in range(1, n-1):
            for j in range(1, n-1):
                best_scenic = max(best_scenic, eval(T, i, j))  # ss
                # if eval(T, i, j):  #fs
                # s += 1
        # print(s)
        print(best_scenic)  # ss

    file = "dane.in"
    # file = "test.in"
    with open(file) as file:
        file = file.readlines()
        T = numpy.array([[int(file[j][i]) for i in range(len(file))]
                         for j in range(len(file))])
    visible(T)


treeHouse()
