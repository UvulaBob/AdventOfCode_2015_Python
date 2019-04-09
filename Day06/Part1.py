import re

grid = []

for y in range(1000):
    newRow = []
    for x in range(1000):
        newRow.insert(x, False)
    grid.append(newRow)

with open("input.txt") as f:
    lines = f.readlines()

activatedLights = 0

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
                grid[y][x] = True
            if instruction == "turn off":
                grid[y][x] = False
            if instruction == "toggle":
                grid[y][x] = not grid[y][x]

for y in range(1000):
    for x in range(1000):
        activatedLights += 1 if grid[y][x] else 0

print(activatedLights)
print("Done!")
