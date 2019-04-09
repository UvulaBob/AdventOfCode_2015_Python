import re

grid = []

for y in range(1000):
    newRow = []
    for x in range(1000):
        newRow.insert(x, 0)
    grid.append(newRow)

with open("input.txt") as f:
    lines = f.readlines()

totalBrightness = 0

for line in lines:
    m = re.match("^(toggle|turn on|turn off) (\\d+),(\\d+) through (\\d+),(\\d+)$", line)
    instruction = m.group(1)
    startX = int(m.group(2))
    startY = int(m.group(3))
    endX = int(m.group(4))
    endY = int(m.group(5))

    for y in range(startY, endY + 1):
        for x in range(startX, endX + 1):
            if instruction == "turn on":
                grid[y][x] += 1
            if instruction == "turn off":
                grid[y][x] -= 1 if grid[y][x] > 0 else 0
            if instruction == "toggle":
                grid[y][x] += 2

for y in range(1000):
    for x in range(1000):
        totalBrightness += grid[y][x]

print(totalBrightness)
print("Done!")
