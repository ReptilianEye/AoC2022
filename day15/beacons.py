class Sensor:
    def __init__(self, sensor, beacon) -> None:
        self.poz = sensor
        self.dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def read_input(file):
    sensors = []
    beacons = []
    for line in file:
        line = line.strip()
        sensor = line[line.find("x"):line.find(":")].split(",")
        sensor = (int(sensor[1][sensor[1].find("=")+1:]),
                  int(sensor[0][sensor[0].find("=")+1:]))
        beacon = line[line.rfind("x"):].split(",")
        beacon = (int(beacon[1][beacon[1].find("=")+1:]),
                  int(beacon[0][beacon[0].find("=")+1:]))
        sensors.append(Sensor(sensor, beacon))
        if beacon not in beacons:
            beacons.append(beacon)

    return sensors, beacons


def gen_ranges_in_line(sensors, query_line):
    counted_ranges = []
    for sensor in sensors:
        dist_left = sensor.dist - abs(sensor.poz[0] - query_line)
        if dist_left >= 0:
            marked = (sensor.poz[1] - dist_left, sensor.poz[1] + dist_left)
            counted_ranges.append(marked)
    counted_ranges.sort()
    return counted_ranges


def merge_ranges(ranges):
    merged_ranges = []
    curr = ranges[0]
    for ran in ranges:
        curr = curr + ran
        if curr[1] >= curr[2]-1:
            curr = (min(curr[0], curr[-2]), max(curr[1], curr[-1]))
        else:
            prev, curr = curr[:2], curr[2:]
            merged_ranges.append(prev)
    merged_ranges.append(curr)
    return merged_ranges


def count_beacon_free(ranges, beacons, query_line):
    result = 0
    for rang in ranges:
        for beacon in list(beacons):
            if beacon[0] == query_line and min(rang) <= beacon[1] and beacon[1] <= max(rang):
                result -= 1
        result += rang[1] - rang[0] + 1
    print(result)


def fs(file, query_line):
    sensors, beacons = read_input(file)
    ranges = gen_ranges_in_line(sensors, query_line)
    ranges = merge_ranges(ranges)
    count_beacon_free(ranges, beacons, query_line)


def ss(file, query_max):
    sensors, beacons = read_input(file)
    for query_line in range(query_max + 1):
        ranges = gen_ranges_in_line(sensors, query_line)
        ranges = merge_ranges(ranges)
        if len(ranges) > 1: #this if is based on observation of input data - only one lacking scanning space was in the middle. It would not work if lackning space was on the edge
            distress = (query_line, ranges[0][1]+1)
            print(distress[1]*4000000+distress[0])
            break


# file = "test.in"
file = "dane.in"

with open(file) as file:
    file = file.readlines()

fs(file, 2_000_000)
ss(file, 4_000_000)
