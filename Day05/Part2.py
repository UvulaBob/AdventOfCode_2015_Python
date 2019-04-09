niceStrings = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    duplicatePairFound = False
    trioFound = False
    for i in range(len(line) - 1):
        pair = line[i] + line[i + 1]
        if not duplicatePairFound:
            pair = line[i] + line[i + 1]
            index = line.find(pair, i + 2)
            if index > 0:
                duplicatePairFound = True
        if not trioFound:
            trio = pair + line[i]
            if trio in line:
                trioFound = True
        if duplicatePairFound and trioFound:
            niceStrings += 1
            break
print(niceStrings)
print("Done!")
