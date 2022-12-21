class Chamber:
    def __init__(self, width, starting_height, stones, dashes, highest_stone=4) -> None:
        self.chamber = [["." for _ in range(width)]
                        for _ in range(starting_height+highest_stone)]
        self.stones = stones
        self.dashes = dashes
        self.s_ht = starting_height
        self.st_it = 0
        self.dash_it = 0
        self.next_s_pos = (len(self.chamber)-starting_height, 2)
        self.last_s_pos = ()

    def show(self):
        for line in self.chamber:
            print("|", end="")
            for el in line:
                print(el, end="")
            print("|", end="")
            print()
        print()

    def draw_stone(self, stone, pos, st_pos=(0, 0)):
        self.chamber[pos[0]][pos[1]] = stone[st_pos[0]][st_pos[1]]
        if st_pos[0] + 1 < len(stone):
            self.draw_stone(stone, (pos[0]+1, pos[1]),
                            (st_pos[0]+1, st_pos[1]))
        if st_pos[1] + 1 < len(stone[st_pos[0]]):
            self.draw_stone(stone, (pos[0], pos[1]+1),
                            (st_pos[0], st_pos[1]+1))

    def vanish_stone(self):
        def vanish_r(stone, pos, st_pos=(0, 0)):
            self.chamber[pos[0]][pos[1]] = "."
            if st_pos[0] + 1 < len(stone):
                vanish_r(stone, (pos[0]+1, pos[1]),
                         (st_pos[0]+1, st_pos[1]))
            if st_pos[1] + 1 < len(stone[st_pos[0]]):
                vanish_r(stone, (pos[0], pos[1]+1),
                         (st_pos[0], st_pos[1]+1))
        stone = self.stones[self.st_it-1]
        vanish_r(stone, self.last_s_pos)

    def next_stone(self):
        stone = self.stones[self.st_it]
        start_pos = (self.next_s_pos[0]-len(stone), self.next_s_pos[1])
        self.draw_stone(stone, start_pos)
        self.last_s_pos = start_pos
        self.st_it = (self.st_it + 1) % len(self.stones)
        #kiedy stawiamy kamien trzeba przesuwac wskaznik na nastepny

stones = [[["#"], ["#"], ["#"], ["#"]], [
    [".", "#", "."], ["#", "#", "#"], [".", "#", "."]]]

chamb = Chamber(7, 3, stones)
chamb.show()
chamb.next_stone()
chamb.show()
chamb.vanish_stone()
chamb.show()
chamb.next_stone()
chamb.show()
chamb.vanish_stone()
chamb.show()
