from Hop import Hop
import re
from itertools import permutations

hops = []
cities = []
shortestRoute = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()

    m = re.search('(\\w+) to (\\w+) = (\\d+)', line)
    a = m.group(1)

    if a not in cities:
        cities.append(a)

    b = m.group(2)

    if b not in cities:
        cities.append(b)

    distance = int(m.group(3))
    shortestRoute += distance
    newHop = Hop(a, b, distance)
    hops.append(newHop)

trips = list(permutations(cities))
for trip in trips:
    possibleShortestTrip = True
    currentTripDistance = 0
    for i in range(0, len(cities) - 1):
        currentCity = trip[i]
        nextCity = trip[i + 1]
        for hop in hops:
            if (hop.a == currentCity and hop.b == nextCity) or \
                    (hop.b == currentCity and hop.a == nextCity):
                currentTripDistance += hop.distance
                break

        if currentTripDistance > shortestRoute:
            possibleShortestTrip = False
            break

    if possibleShortestTrip:
        shortestRoute = currentTripDistance

print(shortestRoute)
print("Done!")





