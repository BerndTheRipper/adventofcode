import re

currentDay = 4

input = open("./day" + str(currentDay) + "/input.txt", "r")
# input = open("./day" + str(currentDay) + "/exampleInputPart1.txt")


def toNumberArray(string):
	output = []
	for match in re.finditer("\d+", string):
		output.append(int(string[match.start():match.end()]))
	return output


currentLine = input.readline()
result = 0


while currentLine != "":
	numberString = currentLine.split(":")[1]
	splitNumberString = numberString.split("|")
	winningNumbers = toNumberArray(splitNumberString[0])
	numbersDrawn = toNumberArray(splitNumberString[1])

	points = 0

	for n in numbersDrawn:
		if n in winningNumbers:
			points = max(1, 2*points)

	result += points
	currentLine = input.readline()

print(result)