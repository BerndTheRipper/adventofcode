import re

exampleExpectedResult = 6
currentDay = 8

exampleInputFile = "exampleInputPart1.txt"
actualInput = "input.txt"

lineRegex = re.compile(r"(\w+)\s=\s\((\w+),\s(\w+)\)")

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
	currentLocation = ""
	path = currentLine[:-1]
	pathIndex = 0
	#skip the current line and the blank one after that
	input.readline()
	currentLine = input.readline()

	lineMatch = lineRegex.match(currentLine).groups()
	locations[lineMatch[0]] = lineMatch[1:]
	currentLocation = "AAA"
	currentLine = input.readline()

	while currentLine != "":
		lineMatch = lineRegex.match(currentLine).groups()
		locations[lineMatch[0]] = lineMatch[1:]

		while currentLocation != "ZZZ":
			if currentLocation == "RFT":
				print("Problem?")
			try:
				if path[pathIndex] == "R":
					currentLocation = locations[currentLocation][1]
				else: currentLocation = locations[currentLocation][0]
				
				pathIndex = (pathIndex + 1) % len(path)
				result += 1
			except KeyError as e:
				if e.args[0] == currentLocation: break
				else: raise e

		currentLine = input.readline()
	
	input.close()
	re.purge()
	return result

if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
	raise Exception("Sample data not delivering expected result!")
else: print("Sample data worked")

print(getSolution(actualInput, currentDay))