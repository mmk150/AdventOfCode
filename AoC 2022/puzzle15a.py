class Sensor:
    def __init__(self, center, beacon):
        self.center = center
        self.beacon = beacon
        self.radius = taxicabMetric(center, beacon)
        self.lines = lineset(center, self.radius)

    def getRadius(self):
        return self.radius

    def getCenter(self):
        return self.center

    def getCrossSection(self, y_val):
        center = self.getCenter()
        lines = self.lines
        print("lines are:")
        print(lines)
        if y_val > center[1]:
            line = lines[1]
            m = line[0]
            b = line[1]
            x = (y_val - b) / m
            dist_center = abs(x - center[0])
            left = center[0] - dist_center
            right = x
            print(center)
            print(x, m, b, dist_center, left, right)
        elif y_val == self.center[1]:
            left = center[0] - self.radius
            right = center[0] + self.radius
        else:
            line = lines[0]
            m = line[0]
            b = line[1]
            x = (y_val - b) / m
            dist_center = abs(x - center[0])
            left = center[0] - dist_center
            right = x
            print(center)
            print(x, m, b, dist_center, left, right)
        interval = [left, right]
        print(interval)
        return interval


def lineset(center, radius):
    diamond_top = (center[0], center[1] - radius)
    diamond_right = (center[0] + radius, center[1])
    diamond_bot = (center[0], center[1] + radius)
    line1 = lineget(diamond_top, diamond_right)
    line2 = lineget(diamond_right, diamond_bot)
    return [line1, line2]


def lineget(point1, point2):
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point2[1] - m * point2[0]
    return (m, b)


def taxicabMetric(point1, point2):
    x_dist = abs(point2[0] - point1[0])
    y_dist = abs(point2[1] - point1[1])
    return x_dist + y_dist


def tballSetSlice(center, radius, row_val):
    tball = set()
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            pos = (center[0] + j, center[1] + i)
            if taxicabMetric(center, pos) <= radius:
                if pos[1] == row_val:
                    tball.add(pos)
    return tball


file = open("puzzle15.txt", "r")
read = file.readlines()

length = len(read)

sensors = []
beacons = []

for i in range(length):
    halves = read[i].split(":")
    temp = halves[0].find("x")
    sensor = halves[0][temp:]
    sensor = sensor.split(",")
    sensor[0] = sensor[0].strip("x=")
    sensor[1] = sensor[1].strip(" y=")
    sensorpos = (int(sensor[0]), int(sensor[1]))
    temp = halves[1].find("x")
    beacon = halves[1][temp:]
    beacon = beacon.split(",")
    beacon[0] = beacon[0].strip("x=")
    beacon[1] = beacon[1].strip(" y=").strip()
    beaconpos = (int(beacon[0]), int(beacon[1]))
    sensors.append(sensorpos)
    beacons.append(beaconpos)
# print(sensors)
# print(beacons)
xmin = 0
xmax = 0
ymin = 0
ymax = 0

for pos in sensors:
    if pos[0] < xmin:
        xmin = pos[0]
    if pos[0] > xmax:
        xmax = pos[0]
    if pos[1] < ymin:
        ymin = pos[1]
    if pos[1] > ymax:
        ymax = pos[1]
for pos in beacons:
    if pos[0] < xmin:
        xmin = pos[0]
    if pos[0] > xmax:
        xmax = pos[0]
    if pos[1] < ymin:
        ymin = pos[1]
    if pos[1] > ymax:
        ymax = pos[1]

width = xmax - xmin
height = ymax - ymin
y_offset = abs(min(ymin, 0))
x_offset = abs(min(xmin, 0))
# print("Offsets:")
# print(y_offset)
# print(x_offset)
adjusted_sensors = []
adjusted_beacons = []
for pos in sensors:
    # print(pos)
    new_pos = (pos[0] + x_offset, pos[1] + y_offset)
    # print(new_pos)
    # print("line 143")
    adjusted_sensors.append(new_pos)

for pos in beacons:
    new_pos = (pos[0] + x_offset, pos[1] + y_offset)
    adjusted_beacons.append(new_pos)


inquiry_row = 2000000
mapped_row = inquiry_row + y_offset

sensor_temp = []

for s in range(len(adjusted_sensors)):
    center = adjusted_sensors[s]
    beacon = adjusted_beacons[s]
    sensor_temp.append(Sensor(center, beacon))
sensor_final = []
for s in sensor_temp:
    center = s.getCenter()
    radius = s.getRadius()
    y_range = range(center[1] - radius, center[1] + radius)
    # print("center is:")
    # print(center)
    # print("radius is:")
    # print(radius)
    # print("yrange is:")
    # print(y_range)
    if mapped_row in y_range:
        sensor_final.append(s)


for x in sensor_final:
    print(x.getCenter())

intervals = []

for s in sensor_final:
    print("center of the sensor is:")
    print(s.center)

    intval = s.getCrossSection(mapped_row)
    intervals.append(intval)
sum = 0
print(intervals)

countset = set()
for x in intervals:
    left = max(int(x[0]), 0)
    for y in range(left, int(x[1])):
        countset.add(y)
count = 0
for x in countset:
    count += 1
    if count > 20:
        break
    print(x)
print("Sum is:")
print(len(countset))
# print("offsets are:")
# print(x_offset)
# print(y_offset)
