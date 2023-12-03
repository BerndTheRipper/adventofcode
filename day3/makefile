CC=gcc
LD=gcc
CFLAGS=
LDFLAGS=

run1:part1
	./part1

run2:part2
	./part2

all:part1 part2

part1: part1.o
	$(LD) -o part1 part1.o $(LDFLAGS)

part1.o: part1.c
	$(CC) -c part1.c -o part1.o $(CFLAGS)


part2: part2.o
	$(LD) -o part2 part2.o $(LDFLAGS)

part2.o: part2.c
	$(CC) -c part2.c -o part2.o $(CFLAGS)

clean:
	rm -f *.o
	rm -f part1
	rm -f part2
	clear