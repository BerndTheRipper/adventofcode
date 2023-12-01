import re

input=open("./day1/input.txt", "r")

currentLine = input.readline()
firstDigitRegex = "(^|\n)\D*\d"
lastDigitRegex = "\d\D*($|\n)"
numberWords = ["", "one","two","three","four","five","six","seven","eight","nine"]
result = 0

while currentLine != "":
	firstDigit = currentLine[re.search(firstDigitRegex, currentLine).end() - 1]
	lastDigit = currentLine[re.search(lastDigitRegex, currentLine).start()]
	result += int(firstDigit+lastDigit)
	currentLine = input.readline()

print(result)