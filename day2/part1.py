import re

input = open("./day2/input.txt", "r")
# input = open("./day2/exampleInputPart1.txt")

currentLine = input.readline()
gameNumber = 1
result = 0

cubeMaximums = {
	"red": 12,
	"green":13,
	"blue":14
}

maxOfOneColor = max(cubeMaximums.values())

while currentLine != "":
	cursorIndex = 0
	lineWithoutGameNumber = currentLine.split(": ")[1]

	draws = lineWithoutGameNumber.split("; ")

	issueFound = False
	for draw in draws:
		cubesDrawn = {}
		for match in re.finditer("(\d+)\s(\w+)", draw):
			groups = match.groups()
			cubesDrawn[groups[1]] = int(groups[0])
		for k,v in cubesDrawn.items():
			try:
				if cubeMaximums[k] < v:
					issueFound = True
			except KeyError:
				issueFound = True
		
		if issueFound:
			break

	if not issueFound:
		result += gameNumber
	
	gameNumber += 1
	currentLine = input.readline()

print(result)