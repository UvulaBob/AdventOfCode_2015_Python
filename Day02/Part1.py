with open("input.txt") as f:
    lines = f.readlines()

totalPaper = 0

for line in lines:
    line = line.strip()
    splitLine = line.split("x")
    length = int(splitLine[0])
    width = int(splitLine[1])
    height = int(splitLine[2])
    
    sides = [length * width, length * height, width * height]
    smallestSide = sides[0]
    for side in sides:
        totalPaper += 2 * side
        if side < smallestSide:
            smallestSide = side
    
    totalPaper += smallestSide
    
    
print(totalPaper)
print("Done!")
