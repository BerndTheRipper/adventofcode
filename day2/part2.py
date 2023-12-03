import re

input = open("./day2/input.txt", "r")
# input = open("./day2/exampleInputPart1.txt") #hasn't changed

currentLine = input.readline()
result = 0

while currentLine != "":
	cursorIndex = 0
	lineWithoutGameNumber = currentLine.split(": ")[1]

	draws = lineWithoutGameNumber.split("; ")

	minimum = {
		"red":0,
		"green":0,
		"blue":0
	}

	for draw in draws:
		cubesDrawn = {}
		for match in re.finditer("(\d+)\s(\w+)", draw):
			groups = match.groups()
			cubeAmount = int(groups[0])
			if minimum[groups[1]] < cubeAmount:
				minimum[groups[1]] = cubeAmount
	
	result += minimum["red"] * minimum["green"] * minimum["blue"]

	currentLine = input.readline()

print(result)