niceStrings = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    badPairInLine = False
    for badPair in ['ab', 'cd', 'pq', 'xy']:
        if badPair in line:
            badPairInLine = True
            break
    if badPairInLine:
        continue
    vowelCount = 0
    for character in line:
        if character in 'aeiou':
            vowelCount += 1
    if vowelCount < 3:
        continue
    doubleLetter = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            doubleLetter = True
            break
    if doubleLetter:
        niceStrings += 1
print(niceStrings)
print("Done!")
