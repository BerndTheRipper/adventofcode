import re

exampleExpectedResult = 114
currentDay = 9

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
		splitLine = currentLine.split(" ")
		intLine = [[]]
		for num in splitLine:
			intLine[0].append(int(num))
		
		allSame = False
		depth = 0
		firstOne = 0
		while not allSame:
			allSame = True
			firstOne = intLine[depth][1] - intLine[depth][0]
			intLine.append([firstOne])
			for i in range(2,len(intLine[depth])):
				difference = intLine[depth][i] - intLine[depth][i-1]
				intLine[depth + 1].append(difference)
				if difference != firstOne:
					allSame = False
			depth += 1
		
		intLine[depth].append(firstOne)
		
		for i in range(len(intLine[-1]) - 1, len(intLine[0]) - 1):
			depth -= 1
			intLine[depth].append(intLine[depth][i] + intLine[depth + 1][i])
		
		result += intLine[0][-1] + intLine[1][-1]

		currentLine = input.readline()
	
	input.close()
	re.purge()
	return result

if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
	raise Exception("Sample data not delivering expected result!")
else: print("Sample data worked")

print(getSolution(actualInput, currentDay))