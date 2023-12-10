#I forgot to switch from part1.py (the original name of this file) to part2.py
#for writing part 2, so my solution for part 1 got lost and here is my solution
# for part 2

import re

exampleExpectedResult = 5905
currentDay = 7

exampleInputFile = "exampleInputPart1.txt"
actualInput = "input.txt"
strengths = "AKQT98765432J"

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

def strongerThan(firstCard, secondCard):
	for i in range(len(firstCard)):
		if firstCard[i] == secondCard[i]: continue
		
		if strengths.index(firstCard[i]) > strengths.index(secondCard[i]):
			return True
		else:
			return False

	return False

def highestCard(deck):
	output = "2"
	strongestIndex = strengths.index("2")
	for card in deck:
		cardIndex = strengths.index(card)
		if cardIndex < strongestIndex:
			output = card
			strongestIndex = cardIndex
	return output

def getSolution(filename, currentDay):
	input = open("./day" + str(currentDay) + "/" + filename, "r")
	result = 0
	currentLine = input.readline()
	hands = {}
	handsByType = {
		"highcard":[],
		"onepair":[],
		"twopair":[],
		"threeofakind":[],
		"fullhouse":[],
		"fourofakind":[],
		"fiveofakind":[]
	}
	while currentLine != "":
		splitLine = currentLine.split(" ")
		currentHand = splitLine[0]
		bid = int(splitLine[1])
		hands[splitLine[0]] = bid

		for i in range(2):
			symbolAmounts = {}
			for symbol in currentHand:
				try:
					symbolAmounts[symbol] += 1
				except KeyError as e:
					if e.args[0] == symbol: symbolAmounts[symbol] = 1
					else: raise e
			
			uniqueSymbolAmount = len(symbolAmounts)
			combination = ""
			jokerTarget = ""
			mostAppearingCardAmount = max(symbolAmounts.values())

			#highCard
			if uniqueSymbolAmount == 5:
				combination = "highcard"
				jokerTarget = highestCard(currentHand)
			#onepair
			elif uniqueSymbolAmount == 4:
				combination = "onepair"
				jokerTarget = highestCard(currentHand)
				for k,v in symbolAmounts.items():
					if v == 2:
						if k == "J": break
						jokerTarget = k
						break
			#twopair
			elif uniqueSymbolAmount == 3 and mostAppearingCardAmount == 2:
				combination = "twopair"
				jokerTarget = ""
				for k,v in symbolAmounts.items():
					if v == 2:
						if k == "J": continue
						if jokerTarget == "":
							jokerTarget = k
							continue
						if strengths.index(k) < strengths.index(jokerTarget):
							jokerTarget = k
							continue
			#three of a kind
			elif uniqueSymbolAmount == 3 and mostAppearingCardAmount == 3:
				combination = "threeofakind"
				jokerTarget = highestCard(currentHand)
				for k,v in symbolAmounts.items():
					if v == 3:
						if k == "J": break
						jokerTarget = k
						break
			#fullhouse
			elif uniqueSymbolAmount == 2 and mostAppearingCardAmount == 3:
				combination = "fullhouse"
				jokerTarget = ""
				for k,v in symbolAmounts.items():
					if v == 3:
						jokerTarget = k
						break
				if jokerTarget == "J":
					for k,v in symbolAmounts.items():
						if v == 2:
							jokerTarget = k
							break
			#fourofakind
			elif uniqueSymbolAmount == 2 and mostAppearingCardAmount == 4:
				jokerTarget = highestCard(currentHand)
				for k,v in symbolAmounts.items():
					if v == 3:
						if k == "J": break
						jokerTarget = k
						break
				combination = "fourofakind"
			#fiveofakind
			elif uniqueSymbolAmount == 1:
				jokerTarget = "A"
				combination = "fiveofakind"
			else:
				print("We might have a problem here")
			updatedHand = ""
			for i in currentHand:
				if i == "J":
					updatedHand += jokerTarget
				else:
					updatedHand += i
			if updatedHand == currentHand:
				break
			currentHand = updatedHand
		handsByType[combination].append(currentLine.split(" ")[0])
		currentLine = input.readline()

	ranking = 1

	#sorting by ranking
	for handList in handsByType.values():
		for k in range(1,len(handList)):
			i = k-1
			while strongerThan(handList[i+1], handList[i]) and i >= 0:
				temp = handList[i]
				handList[i] = handList[i+1]
				handList[i+1] = temp
				i-=1
		for hand in handList:
			result += hands[hand] * ranking
			ranking += 1

	print("done sorting")
	input.close()
	return result

if getSolution(exampleInputFile, currentDay) != exampleExpectedResult:
	raise Exception("Sample data not delivering expected result!")
else: print("Sample data worked")

print(getSolution(actualInput, currentDay))