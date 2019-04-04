with open("input.txt") as f:
    lines = f.readlines()

totalRibbon = 0

for line in lines:
    line = line.strip()
    splitLine = line.split("x")
    length = int(splitLine[0])
    width = int(splitLine[1])
    height = int(splitLine[2])

    measurements = [length, width, height]
    measurements.sort()
    totalRibbon += (measurements[0] * 2) + (measurements[1] * 2)
    totalRibbon += measurements[0] * measurements[1] * measurements[2]

print(totalRibbon)
print("Done!")
