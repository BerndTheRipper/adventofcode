//Giving up trying to solve this in c and 2d array logic, switching to python and regex

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
	// FILE *input = fopen("input.txt", "r");
	FILE *input = fopen("exampleInputPart1.txt", "r");
	if(input == NULL){
		printf("Failed to open input file.\n");
		return EXIT_FAILURE;
	}

	char **lines;
	unsigned int lineLength = 0;
	unsigned int solution = 0;
	for(char currentChar = getc(input); (unsigned char) currentChar != '\n' && currentChar != EOF; lineLength++){
		currentChar = (char) getc(input);
	}
	rewind(input);

	//Allocation of the whole structure
	lines = malloc(lineLength * sizeof(char*));
	if(lines == NULL){
		fclose(input);
		printf("Memory allocation error for the whole file\n");
		return EXIT_FAILURE;
	}

	//Allocation of the individual lines
	for(int line = 0; line < lineLength; line++){
		lines[line] = malloc((lineLength + 1) * sizeof(char));

		//Clearing all that was allocated
		if(lines[line] == NULL){
			for(int lineToClear = 0; lineToClear < line; lineToClear++){
				free(lines[lineToClear]);
			}
			free(lines);
			fclose(input);
			printf("Memory allocation error for the lines.\n");
			return EXIT_FAILURE;
		}


	}
	
	for(int y = 0; y <= lineLength; y++){
		if(y < lineLength){
			fgets(lines[y], lineLength + 1, input);
			char currentChar = fgetc(input);
			if((currentChar != '\n' && y < lineLength - 1) || (currentChar != EOF && y == lineLength - 1)){
				printf("Something weird happened here. %d %d %d\n", y, (currentChar != '\n' && y < lineLength - 1), (currentChar != EOF && y == lineLength - 1));
			}
		}
		if(!y){
			continue;
		}
		y--;
		int numberFound = 0;
		int numberLength = 0;
		for(int x = 0; x < lineLength; x++){
			if(lines[y][x] >= '0' && lines[y][x] <= '9'){
				numberFound = numberFound * 10 + (int) (lines[y][x] - '0');
				numberLength++;
			}
			//If a number has been found and at our current point there is no number
			else if(numberFound){
				short foundSymbol = 0;
				for(int xOffset = -numberLength - 1; xOffset <= 0 && !foundSymbol; xOffset++){
					int xToCheck = x + xOffset;
					if(xToCheck < 0 || xToCheck >= lineLength) continue;
					for(int yOffset = -1; yOffset <= 1 && !foundSymbol; yOffset++){
						int yToCheck = y + yOffset;
						if(yToCheck < 0 || yToCheck >= lineLength) continue;
						// if(yOffset == 0 && (xOffset > -numberLength && xOffset < 0)) continue;
						if(lines[yToCheck][xToCheck] != '.' && (yOffset != 0 || lines[yToCheck][xToCheck] < '0' || lines[yToCheck][xToCheck] > '9')) {
							if(lines[yToCheck][xToCheck] != '*' && lines[yToCheck][xToCheck] != '#' && lines[yToCheck][xToCheck] != '=' && lines[yToCheck][xToCheck] != '&' && lines[yToCheck][xToCheck] != '@')
								printf("Symbol found: %c in line %d symbol %d looking at x%d y%d\n", lines[yToCheck][xToCheck], yToCheck, xToCheck, x, y);
							//TODO continue here
							foundSymbol = 1;
							
						}
					}
				}
				unsigned int oldSolution = solution;
				if(foundSymbol) solution += numberFound;
				if(solution < oldSolution) printf("Problem");
				numberFound = 0;
				numberLength = 0;
			}
		}
		y++;
	}

	printf("Line length: %d\n", lineLength);
	printf("Solution: %u\n", solution);
	for(int lineToClear = 0; lineToClear < lineLength; lineToClear++){
		free(lines[lineToClear]);
	}
	free(lines);
	fclose(input);
	return EXIT_SUCCESS;
}