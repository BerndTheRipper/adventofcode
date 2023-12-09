import re
import math

exampleExpectedResult = 71503
currentDay = 6

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
	times = re.findall("\d+", currentLine)
	currentLine = input.readline()
	distances = re.findall("\d+", currentLine)
	if len(times) != len(distances):
		print("Something is wrong")
	
	time = ""
	distance = ""
	for t in times:
		time += t
	for d in distances:
		distance += d
	
	time = int(time)
	distance = int(distance)
	lowerEnd = int(time/2 - math.sqrt((-time/2)**2 - distance) + 1)
	upperEnd = math.ceil(time/2 + math.sqrt((-time/2)**2 - distance) - 1)
	result = upperEnd - lowerEnd + 1
	if result == 0:
		result = upperEnd - lowerEnd + 1
	
	input.close()
	return result

if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
	raise Exception("Sample data not delivering expected result!")
else: print("Sample data worked")

print(getSolution(actualInput, currentDay))