import re

def checkNumber(string:str, startIndex:int, toTheRight:bool)->str:
	checkNumberOutput:str = ""
	direction = -1 + 2*toTheRight
	while startIndex >= 0 and startIndex < len(string) and '0' <= string[startIndex] and string[startIndex] <= '9':
		if direction < 0:
			checkNumberOutput = string[startIndex] + checkNumberOutput
		else:
			checkNumberOutput += string[startIndex]
		startIndex += direction
	
	return checkNumberOutput

def checkNumberFromMid(string:str, middleIndex:int):
	output = []

	if('0' <= string[middleIndex] and string[middleIndex] <= '9'):
		output.append(string[middleIndex])
		offset = -1
		while 0 <= middleIndex + offset and '0' <= string[middleIndex + offset] and string[middleIndex + offset] <= '9':
			output[0] = string[middleIndex + offset] + output[0]
			offset -= 1
		offset = 1
		while middleIndex + offset < len(string) and '0' <= string[middleIndex + offset] and string[middleIndex + offset] <= '9':
			output[0] += string[middleIndex + offset]
			offset += 1

	else:
		leftResult = checkNumber(string, middleIndex - 1, False)
		if leftResult != "": output.append(leftResult)

		rightResult = checkNumber(string, middleIndex + 1, True)
		if rightResult != "": output.append(rightResult)

	for i in range(len(output)):
		output[i] = int(output[i])
	return output

input = open("./day3/input.txt", "r")
# input = open("./day3/exampleInputPart1.txt")

currentLine = input.readline()[:-1]
lines = []
result = 0

while currentLine != "":
	lines.append(currentLine)
	currentLine = input.readline()[:-1]


for y, line in enumerate(lines):
	for match in re.finditer("\\*", line):
		gearRatio = 0
		stringsAroundGear = (line[:match.start()], line[match.end():])
		matchesAroundGear = (re.search("\\d+$", stringsAroundGear[0]), re.search("^\\d+", stringsAroundGear[1]))
		valuesAroundGear = []

		for i,roundmatch in enumerate(matchesAroundGear):
			if roundmatch == None: continue
			valuesAroundGear.append(int(stringsAroundGear[i][roundmatch.start():roundmatch.end()]))

		yOffset = -1
		while yOffset <= 1:
			yToCheck = y + yOffset
			if yToCheck < 0 or yToCheck >= len(lines): continue

			resultsFromLine = checkNumberFromMid(lines[yToCheck], match.start())
			for resultFromLine in resultsFromLine:
				valuesAroundGear.append(resultFromLine)
			yOffset+=2
		
		if len(valuesAroundGear) > 1:
			gearRatio = valuesAroundGear[0]
			valueIndex = 1
			while valueIndex < len(valuesAroundGear):
				gearRatio *= valuesAroundGear[valueIndex]
				valueIndex += 1
			result += gearRatio



print(result)
input.close()