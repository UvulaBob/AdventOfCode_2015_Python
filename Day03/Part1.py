santaX = 0
santaY = 0

visitedPoints = {str(santaX) + ", " + str(santaY): 1}

with open("input.txt") as f:
    line = f.readline()

for character in line:
    if character == '^':
        santaY -= 1
    if character == '<':
        santaX -= 1
    if character == '>':
        santaX += 1
    if character == 'v':
        santaY += 1
    visitedPoints[str(santaX) + ", " + str(santaY)] = 1

print(len(visitedPoints))
print("Done!")
    