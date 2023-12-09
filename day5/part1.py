import re

currentDay = 5

input = open("./day" + str(currentDay) + "/input.txt", "r")
# input = open("./day" + str(currentDay) + "/exampleInputPart1.txt")


def toNumberArray(string):
	output = []
	for match in re.finditer("\d+", string):
		output.append(int(string[match.start():match.end()]))
	return output

def stringArrayToIntArray(arr):
	output = []
	for string in arr:
		output.append(int(string))
	return output

currentLine = input.readline()
result = -1
seedNumbers = [[]]
pathsToLocations = []
rawMaps = {}
mappings = {}
currentMap = ""

while currentLine != "":
	numberMatch = re.findall("\d+", currentLine)
	if currentLine.startswith("seeds:"):
		pathsToLocations.append(toNumberArray(currentLine))
	elif "map" in currentLine:
		currentMap = currentLine.split("map")[0]
	elif len(numberMatch) and currentMap != "":
		try:
			rawMaps[currentMap].append(stringArrayToIntArray(numberMatch))
		except KeyError:
			rawMaps[currentMap] = [stringArrayToIntArray(numberMatch)]
	
	currentLine = input.readline()

lastMapName = ""
for mapName, mapData in rawMaps.items():
	mappings[mapName] = {}
	seedPath = []
	pathToFind = pathsToLocations[-1]

	if len(pathsToLocations):
		pathToFind = pathsToLocations[-1]
	
	for seed in pathToFind:
		mapping = seed
		for mapLine in mapData:
			if mapLine[1] <= seed and seed < mapLine[1] + mapLine[2]:
				mapping = mapLine[0] - mapLine[1] + seed
		seedPath.append(mapping)
	
	
	pathsToLocations.append(seedPath)
	lastMapName = mapName

result = min(pathsToLocations[-1])
print(result)