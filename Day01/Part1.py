floor = 0
file = open("input.txt", "r")
first_line = file.readline()
for character in first_line:
    if character == "(":
        floor += 1
    else:
        floor -= 1
print(floor)
print("Done!")


