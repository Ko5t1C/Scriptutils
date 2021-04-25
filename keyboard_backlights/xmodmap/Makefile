all: enablexmodmap

enablexmodmap: enablexmodmap.o main.o
		gcc -o enablexmodmap enablexmodmap.o main.o

enablexmodmap.o: enablexmodmap.c
		gcc -o enablexmodmap.o -c enablexmodmap.c -W -Wall -ansi -pedantic

main.o: main.c enablexmodmap.h
		gcc -o main.o -c main.c -W -Wall -ansi -pedantic

clean:
		rm -rf *.o

clear: clean
		rm -rf enablexmodmap
