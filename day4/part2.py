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
cardNumber = 0

winningNumbers = []
numbersDrawn = []
howManyScratchers = [1]

while currentLine != "":
	numberString = currentLine.split(":")[1]
	splitNumberString = numberString.split("|")
	winningNumbers.append(toNumberArray(splitNumberString[0]))
	numbersDrawn.append(toNumberArray(splitNumberString[1]))

	copiesToBeMade = 0
	try:
		howManyScratchers[cardNumber]
	except IndexError:
		howManyScratchers.append(1)
	
	for n in numbersDrawn[cardNumber]:
		if n in winningNumbers[cardNumber]:
			copiesToBeMade += 1

	for i in range(copiesToBeMade):
		try:
			howManyScratchers[cardNumber + i + 1] += howManyScratchers[cardNumber]
		except IndexError:
			howManyScratchers.append(1 + howManyScratchers[cardNumber])
		
	result += howManyScratchers[cardNumber]
	cardNumber += 1
	currentLine = input.readline()

print(result)