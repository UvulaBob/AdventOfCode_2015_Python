santaX = 0
santaY = 0

roboSantaX = 0
roboSantaY = 0

visitedPoints = {str(santaX) + ", " + str(santaY): 1}

santaTurn = True

with open("input.txt") as f:
    line = f.readline()

for character in line:
    if character == '^':
        if santaTurn:
            santaY -= 1
        else:
            roboSantaY -= 1
    if character == '<':
        if santaTurn:
            santaX -= 1
        else:
            roboSantaX -= 1
    if character == '>':
        if santaTurn:
            santaX += 1
        else:
            roboSantaX += 1
    if character == 'v':
        if santaTurn:
            santaY += 1
        else:
            roboSantaY += 1

    visitedPoints[str(santaX) + ", " + str(santaY)] = 1
    visitedPoints[str(roboSantaX) + ", " + str(roboSantaY)] = 1

    santaTurn = not santaTurn

print(visitedPoints)
print(len(visitedPoints))
print("Done!")
    