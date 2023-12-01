import re

input=open("./day1/input.txt", "r")

currentLine = input.readline()
firstDigitRegex = "(^|\n)\D*\d"
lastDigitRegex = "\d\D*($|\n)"
numberRegex = "\d|one|two|three|four|five|six|seven|eight|nine"
numberWords = ["", "one","two","three","four","five","six","seven","eight","nine"]
result = 0

while currentLine != "":
	findAllResult = re.findall(numberRegex, currentLine)
	firstNumberResult = re.search(numberRegex, currentLine)
	if(firstNumberResult == None):
		print("Problem match")
	firstMatch = currentLine[firstNumberResult.start():firstNumberResult.end()]
	
	lastMatch = ""
	for i in range(1,len(currentLine)+1):
		currentMatch = re.search(numberRegex, currentLine[-i:])
		if currentMatch != None:
			lastMatch = currentLine[-i:][currentMatch.start():currentMatch.end()]
			break
	if(lastMatch == ""):
		print("Last match ist leer")
	lineResult = 0


	try:
		lineResult += 10 * int(firstMatch)
	except ValueError:
		lineResult += 10 * numberWords.index(firstMatch)
	
	if(lineResult < 10 or lineResult > 90): 
		print("Problem")
	
	try:
		lineResult += int(lastMatch)
	except ValueError:
		lineResult += numberWords.index(lastMatch)
	
	if(lineResult < 10 or lineResult > 99):
		print("Problem 2")
	
	result += lineResult
	currentLine = input.readline()

print(result)