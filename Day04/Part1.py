import hashlib

secretKey = 'iwrupvqb'
index = 0

result = ""

while result[0:5] != '00000':
    index += 1
    stringToHash = secretKey + str(index)
    result = hashlib.md5(stringToHash.encode()).hexdigest()

print(index)
print("Done!")

