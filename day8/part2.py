#got the idea to use lcm from reddit, so not sure if this counts

import re
import math

exampleExpectedResult = 6
currentDay = 8

exampleInputFile = "exampleInputPart2.txt"
actualInput = "input.txt"

lineRegex = re.compile(r"(\S+)\s=\s\((\S+),\s(\S+)\)")

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
	input = open("./day" + str(currentDay) + "/" + filename, "r")
	result = 0
	currentLine = input.readline()
	
	#(location, [choices])
	locations = {}
	path = currentLine[:-1]
	pathIndex = 0
	#skip the current line and the blank one after that
	input.readline()
	currentLine = input.readline()

	pathLocations = []

	while currentLine != "":
		lineMatch = lineRegex.match(currentLine).groups()
		locations[lineMatch[0]] = lineMatch[1:]

		if lineMatch[0][2] == "A":
			pathLocations.append(lineMatch[0])

		currentLine = input.readline()
	
	doneWalking = False
	resultsWithZ = [[],[],[],[],[],[]]
	while not doneWalking:
		doneWalking = True
		if result == 19630:
			print("lookie lookie")
		for i in range(len(pathLocations)):
			location = pathLocations[i]
			if path[pathIndex] == "R":
				pathLocations[i] = locations[location][1]
			elif path[pathIndex] == "L":
				pathLocations[i] = locations[location][0]
			else:
				print("Problem here")
			if pathLocations[i][2] != "Z":
				doneWalking = False
			else:
				resultsWithZ[i].append(result + 1)
			if location == "fqt":
				print("check here")
		
		checkOutTheResults = True
		for results in resultsWithZ:
			if len(results) < 5:
				checkOutTheResults = False
		
		deltas = []
		if checkOutTheResults:
			for results in resultsWithZ:
				delta = results[-1] - results[-2]
				appendIt = True
				for i in range(1, len(results)):
					if results[i] - results[i-1] != delta:
						appendIt = False
				if appendIt:
					deltas.append(delta)
				else:
					deltas.append(-1)
			result = math.lcm(*deltas)
			break
		result += 1
		pathIndex = (pathIndex + 1) % len(path)
		i = 0

	input.close()
	re.purge()
	return result

# if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
# 	raise Exception("Sample data not delivering expected result!")
# else: print("Sample data worked")

print(getSolution(actualInput, currentDay))