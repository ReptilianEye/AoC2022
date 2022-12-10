base = {2: 1, 2 + 1j: 1 + 1j, 2 + 2j: 1 + 1j, 1 + 2j: 1 + 1j}
deltas = {k * 1j**i: v * 1j**i for k, v in base.items() for i in range(4)}
directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
instructions = [x.split() for x in open("dane.in").readlines()]


def tail_moves(rope_length):
    seen = []
    rope = [0] * rope_length
    for direction, count in instructions:
        for _ in range(int(count)):
            rope[0] += directions[direction]
            for i in range(1, len(rope)):
                rope[i] += deltas[rope[i - 1] - rope[i]
                                  ] if abs(rope[i - 1] - rope[i]) >= 2 else 0
            if rope[-1] not in seen:
                print([int(rope[-1].imag),int(rope[-1].real)])
                seen.append(rope[-1])
    return seen


print(len(tail_moves(2)))
print(len(set(tail_moves(10))))
