all: keyled

keyled: keyled.o main.o
		gcc -o keyled keyled.o main.o

keyled.o: keyled.c
		gcc -o keyled.o -c keyled.c -W -Wall -ansi -pedantic

main.o: main.c keyled.h
		gcc -o main.o -c main.c -W -Wall -ansi -pedantic

clean:
		rm -rf *.o

clear: clean
		rm -rf keyled
