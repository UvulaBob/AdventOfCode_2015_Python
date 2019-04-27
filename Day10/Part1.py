string = list("3113322113")

for iteration in range(40):
    newString = list("")
    currentIndex = 0
    while currentIndex < len(string):
        currentCharacter = string[currentIndex]
        currentCharacterCount = 1
        lookAheadIndex = currentIndex + 1
        while lookAheadIndex < len(string):
            if string[lookAheadIndex] == currentCharacter:
                currentCharacterCount += 1
                lookAheadIndex += 1
            else:
                break
        newString.append(str(currentCharacterCount))
        newString.append(str(currentCharacter))
        currentIndex = lookAheadIndex
    string = newString

print(len(string))
print("Done!")
