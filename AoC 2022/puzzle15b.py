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
        if y_val > center[1]:
            line = lines[1]
            m = line[0]
            b = line[1]
            x = (y_val - b) / m
            dist_center = abs(x - center[0])
            left = center[0] - dist_center
            right = x
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
        interval = [left, right]
        return interval

    def getXval(self, yval):
        center = self.getCenter()
        lines = self.lines
        if yval > center[1]:
            line = lines[1]
            m = line[0]
            b = line[1]
            x = (yval - b) / m
        else:
            line = lines[0]
            m = line[0]
            b = line[1]
            x = (yval - b) / m
        return x


def getPerim(center, radius):
    perimSet = []
    radius = radius + 1
    for i in range(0, radius):
        point_q1 = (center[0] + i, center[1] - radius + i)
        point_q2 = (center[0] - i, center[1] - radius + i)
        point_q3 = (center[0] - i, center[1] + radius - i)
        point_q4 = (center[0] + i, center[1] + radius - i)
        perimSet.append(point_q1)
        perimSet.append(point_q2)
        perimSet.append(point_q3)
        perimSet.append(point_q4)
    return perimSet


def NotInDiamondCheck(position, sensor):
    x_val = position[0]
    y_val = position[1]
    if taxicabMetric(position, sensor.getCenter()) > sensor.getRadius():
        return True
    else:
        return False
    # sensorx=sensor.getXval(y_val)
    # interval=sensor.getCrossSection(y_val)
    # print(position)
    # print(interval)
    # print("line 78")
    # if x_val>=interval[0] and x_val<=interval[1]:
    #    return False
    # return True


def beaconCheck(position, sensor_list):
    x = position[0]
    y = position[1]
    pos1 = (x + 1, y)
    ispos1 = True
    pos2 = (x - 1, y)
    ispos2 = True
    pos3 = (x, y + 1)
    ispos3 = True
    pos4 = (x, y - 1)
    ispos4 = True
    for s in sensor_list:
        if ispos1:
            ispos1 = NotInDiamondCheck(pos1, s)
        if ispos2:
            ispos2 = NotInDiamondCheck(pos2, s)
        if ispos3:
            ispos3 = NotInDiamondCheck(pos3, s)
        if ispos4:
            ispos4 = NotInDiamondCheck(pos4, s)
    if not ispos1 and not ispos2 and not ispos3 and not ispos4:
        return True
    else:
        return False


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
# print(xmin)
# print(xmax)
# print(ymin)
# print(ymax)
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


# inquiry_row=2000000
# mapped_row=inquiry_row+y_offset

sensor_final = []

for s in range(len(adjusted_sensors)):
    center = adjusted_sensors[s]
    beacon = adjusted_beacons[s]
    sensor_final.append(Sensor(center, beacon))
candidates = dict()
for x in sensor_final:
    perim = getPerim(x.getCenter(), x.getRadius())
    for cand in perim:
        if candidates.get(cand) != None:
            candidates[cand] += 1
        else:
            candidates.update({cand: 1})
almost_final_candidates = []
for k in candidates:
    value = candidates[k]
    if value >= 3:
        almost_final_candidates.append(k)
        # print(k[0]-x_offset,k[1]-y_offset)
        # print(value)
temp = []
for a in almost_final_candidates:
    if a not in adjusted_beacons:
        temp.append(a)
# print(temp)
final_candidates = []
for f in temp:
    isNotInAny = True
    for s in sensor_final:
        isNotInAny = NotInDiamondCheck(f, s)
        # if f==(16,11):
        # print("Debug!!")
        # print("Beacon position:")
        # print(f)
        # print("It is not in any diamonds:")
        # print(isNotInAny)
        # print("The diamond it may or may not be in:")
        # print("Center:")
        # print(s.getCenter())
        # print("Radius:")
        # print(s.getRadius())
        if isNotInAny == False:
            break
    if isNotInAny:
        final_candidates.append(f)
# print(final_candidates)
for f in final_candidates:
    result = beaconCheck(f, sensor_final)
    if result:
        answer = f
        break

#print("x and y offsets:")
#print(x_offset)
#print(y_offset)
#print("Beacon:")
xco = answer[0] - x_offset
yco = answer[1] - y_offset
#print(xco, yco)
#print("Tuning frequency:")
calc = 4000000 * xco + yco
print(calc)
