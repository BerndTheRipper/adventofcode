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

def convert(destination, source, seed):
	return destination - source + seed

def getSolution(filename, currentDay):
	input = open("./day" + str(currentDay) + "/" + filename + ".txt", "r")
	result = 0
	currentLine = input.readline()
	stepsToLocations = [[]]
	rawMaps = {}
	currentMap = ""

	while currentLine != "":
		numberMatch = re.findall("\d+", currentLine)
		if currentLine.startswith("seeds:"):
			for i in range(0, len(numberMatch), 2):
				stepsToLocations[0].append(stringArrayToIntArray(numberMatch[i:i+2]))
		elif "map" in currentLine:
			currentMap = currentLine.split("map")[0]
		elif len(numberMatch) and currentMap != "":
			try:
				rawMaps[currentMap].append(stringArrayToIntArray(numberMatch))
			except KeyError:
				rawMaps[currentMap] = [stringArrayToIntArray(numberMatch)]
		
		currentLine = input.readline()
	
	for mapData in rawMaps.values():
		nextSeedStep = []
		currentSteps = stepsToLocations[-1]
		for step in currentSteps:
			stepStart = step[0]
			stepEnd = step[0] + step[1]
			doneWithStep = False
			for mapLine in mapData:
				mapStart = mapLine[1]
				mapEnd = mapLine[1] + mapLine[2]
				if doneWithStep: break
				#small seed in map				big seed in map
				if mapStart <= stepStart and stepEnd <= mapEnd:
					convertedStart = convert(mapLine[0], mapStart, stepStart)
					nextSeedStep.append([convertedStart, step[1]])
					doneWithStep = True
				#small seed in map,												big one outside
				elif mapStart <= stepStart and stepStart < mapEnd and mapEnd < stepEnd:
					convertedStart = convert(mapLine[0], mapStart, stepStart)
					convertedEnd = mapEnd - stepStart
					if step[1] <= convertedEnd:
						print("Problem 2")
					nextSeedStep.append([convertedStart, convertedEnd])
					step[0]  = mapEnd
					step[1] -= convertedEnd
				#small seed outside of map, 	big one inside
				elif stepStart < mapStart and mapStart < stepEnd and stepEnd <= mapEnd:
					convertedStart = convert(mapLine[0], mapStart, mapStart)
					convertedEnd = stepEnd - mapStart
					nextSeedStep.append([convertedStart, convertedEnd])
					step[1] -= convertedEnd
				#small seed outside of map and big seed outside of map but still some inside
				elif stepStart < mapStart and mapEnd < stepEnd:
					convertedStart = convert(mapLine[0], mapStart, mapStart)
					convertedEnd = mapLine[2]
					nextSeedStep.append([convertedStart, convertedEnd])
					currentSteps.append([mapEnd, stepEnd - mapEnd])
					step[1] = mapStart - stepStart
			
			if not doneWithStep: nextSeedStep.append(step)
				
		stepsToLocations.append(nextSeedStep)

	locationArray = []
	for location in stepsToLocations[-1]:
		locationArray.append(location[0])
	result = min(locationArray)
	input.close()
	return result

if getSolution("exampleInputPart1", 5) != 46:
	raise Exception("Regression problem")
else: print("Sample data worked")

print(getSolution("input", 5))