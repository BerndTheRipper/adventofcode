import re


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

def getSolution(filename, currentDay):
	input = open("./day" + str(currentDay) + "/" + filename + ".txt", "r")
	currentLine = input.readline()
	result = -1
	pathsToLocations = [[]]
	rawMaps = {}
	currentMap = ""

	while currentLine != "":
		numberMatch = re.findall("\d+", currentLine)
		if currentLine.startswith("seeds:"):
			for i in range(0, len(numberMatch), 2):
				pathsToLocations[0].append(stringArrayToIntArray(numberMatch[i:i+2]))
		elif "map" in currentLine:
			currentMap = currentLine.split("map")[0]
		elif len(numberMatch) and currentMap != "":
			try:
				rawMaps[currentMap].append(stringArrayToIntArray(numberMatch))
			except KeyError:
				rawMaps[currentMap] = [stringArrayToIntArray(numberMatch)]
		
		currentLine = input.readline()


	for mapData in rawMaps.values():
		seedPath = []
		pathToFind = pathsToLocations[-1]

		for seedPair in pathToFind:
			if seedPair[0] == 79:
				print("Break?")
			doneWithSeedPair = False
			for mapLine in mapData:
				if doneWithSeedPair:
					continue

				if -(mapLine[0] - mapLine[1]) > seedPair[0]:
					print("Math problem?")
				#smaller and bigger seed in map
				if mapLine[1] <= seedPair[0] and seedPair[0] + seedPair[1] <= mapLine[1] + mapLine[2]:
					seedPath.append([mapLine[0] - mapLine[1] + seedPair[0], seedPair[1]])
					doneWithSeedPair = True
				#smaller seed in map, 																			bigger one outside
				elif mapLine[1] <= seedPair[0] and seedPair[0] < mapLine[1] + mapLine[2] and mapLine[1] + mapLine[2] < seedPair[0] + seedPair[1]:
					deltaMapLineEndSeedPair0 = mapLine[1] + mapLine[2] - seedPair[0]
					seedPath.append([mapLine[0] - mapLine[1] + seedPair[0], deltaMapLineEndSeedPair0])
					seedPair[0] += deltaMapLineEndSeedPair0 #todo test if this makes it equal to mapLIne[1] + mapLIne[2]
					if seedPair[0] != mapLine[1] + mapLine[2]:
						print("Problem")
					seedPair[1] -= deltaMapLineEndSeedPair0
					if seedPath[-1][0] <= 0:
						print("Problem1")
				#smaller seed outside of map, 		bigger one inside
				elif seedPair[0] < mapLine[1] and mapLine[1] < seedPair[0] + seedPair[1] and seedPair[0] + seedPair[1] <= mapLine[1] + mapLine[2]:
					#what smaller seed is so far outside that seedPair is bigger than mapLine solved?
					seedPath.append([mapLine[0], seedPair[0] + seedPair[1] - mapLine[1]])
					if seedPath[-1][0] <= 0:
						print("Problem2?")
					seedPair[1] = (mapLine[2] + mapLine[1]) - (seedPair[0] + seedPair[1])
				#smaller seed outside of map	and bigger seed outside of map
				elif seedPair[0] < mapLine[1] and mapLine[1] + mapLine[2] <= seedPair[0] + seedPair[1]:
					seedPath.append([mapLine[0], mapLine[2]])
					pathToFind.append([mapLine[1] + mapLine[2], seedPair[0] + seedPair[1] - mapLine[1] + mapLine[2]])
					seedPair[1] = mapLine[1] - seedPair[0]
					if seedPath[-1][0] <= 0:
						print("Problem3")
			if not doneWithSeedPair:
				seedPath.append(seedPair)
		pathsToLocations.append(seedPath)


	testArray = []
	for path in pathsToLocations[-1]:
		testArray.append(path[0])
	result = min(testArray)
	input.close()

	for k,path in enumerate(pathsToLocations[6]):
		if path[0] <= 1735512469 and 1735512469  < path[0] + path[1]:
			print("should be good")
		if 1735512469 <= path[0] and path[0] < 1735512469 + 459590666:
			print("I hate this day and the fact that I'm two days late already")
	return result

if getSolution("exampleInputPart1", 5) != 46:
	raise Exception("Regression problem")
else: print("Sample data worked")

print(getSolution("input", 5))
