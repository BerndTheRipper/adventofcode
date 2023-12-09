import re

exampleExpectedResult = 0
currentDay = -1

exampleInputFile = "exampleInputPart1.txt"
actualInput = "input.txt"

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

	while currentLine != "":
		currentLine = input.readline()
	
	return result

if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
	raise Exception("Sample data not delivering expected result!")
else: print("Sample data worked")

print(getSolution(actualInput, currentDay))