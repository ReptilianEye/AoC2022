def solve_fs(file):
    cycle = 0
    x = 1
    breakpoint = 20
    s = 0
    for line in file:
        oper = line.strip().split()
        if oper[0] == "noop":
            inc = 0
            cycle += 1
        else:
            inc = int(oper[1])
            cycle += 2

        if cycle >= breakpoint:
            s += x*breakpoint
            breakpoint += 40
        x += inc

    print(s)
    # return s


def print_screen(screen):
    for line in screen:
        for el in line:
            print(el, end="")
        print()


def solve_ss(file):
    f_i = 0  # file iterator
    oper_left = 0  # operations left to start next
    inc = 0  # inc to X by operation
    screen = [["" for _ in range(40)] for _ in range(6)]
    sprite = (0, 1, 2)
    for cycle in range(240):
        if oper_left == 0 and f_i < len(file):
            sprite = tuple(range(sprite[0]+inc, sprite[0]+inc+3))
            oper = file[f_i].strip().split()
            f_i += 1
            if oper[0] == "noop":
                oper_left = 1
                inc = 0
            else:  # operation is addx
                oper_left = 2
                inc = int(oper[1])
        if cycle % 40 in sprite:
            screen[cycle//40][cycle % 40] = "#"
        else:
            screen[cycle//40][cycle % 40] = "."

        oper_left -= 1
    print_screen(screen)


# file = "test.in"
file = "dane.in"

with open(file) as file:
    file = file.readlines()
    solve_fs(file)
    solve_ss(file)
