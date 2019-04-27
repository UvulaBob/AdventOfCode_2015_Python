with open("input.txt") as f:
    lines = f.readlines()

totalLiterals = 0
totalNewLiterals = 0

for line in lines:
    line = line.strip("\n")
    totalLiterals += len(line)
    newLineLiterals = 2

    for character in line:
        newLineLiterals += 1
        if character == "\"" or character == "\\":
            newLineLiterals += 1

    totalNewLiterals += newLineLiterals


print(totalNewLiterals)
print(totalLiterals)
print(totalNewLiterals - totalLiterals)
print("Done!")
