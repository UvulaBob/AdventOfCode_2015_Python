with open("input.txt") as f:
    lines = f.readlines()

totalLiterals = 0
totalCharacters = 0

for line in lines:
    line = line.strip("\n")
    totalLiterals += len(line)
    charactersInLine = len(line) - 2

    i = 1
    while i < len(line) - 1:
        firstCharacter = line[i:i + 1]
        if firstCharacter == "\\":
            secondCharacter = line[i + 1:i + 2]
            if secondCharacter == "x":
                charactersInLine -= 3
                i += 3
            else:
                charactersInLine -= 1
                i += 1
        i += 1

    totalCharacters += charactersInLine

print(totalLiterals)
print(totalCharacters)
print(totalLiterals - totalCharacters)
print("Done!")
