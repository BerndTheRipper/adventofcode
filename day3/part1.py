import re

input = open("./day3/input.txt", "r")
# input = open("./day3/exampleInputPart1.txt")

currentLine = input.readline()[:-1]
lines = []
result = 0
lineNumber = 0
lineLength = len(currentLine) - 1

while currentLine != "":
	lines.append(currentLine)
	currentLine = input.readline()[:-1]


for y, line in enumerate(lines):
	for match in re.finditer("\\d+", line):
		addToResult = False
		if match.start() != 0 and line[match.start() - 1] != '.': addToResult = True
		if match.end() < lineLength and line[match.end()] != '.' : addToResult = True
		if y > 0 and re.search("[^.]", lines[y - 1][max(match.start()-1, 0):min(match.end()+1, len(line) - 1)]) != None: addToResult = True
		if y < len(lines) - 1 and re.search("[^.]", lines[y + 1][max(match.start()-1, 0):min(match.end()+1, len(line) - 1)]) != None: addToResult = True
		
		if addToResult:
			print("added " + line[match.start():match.end()] + " to result")
			result += int(line[match.start():match.end()])


print(result)
input.close()