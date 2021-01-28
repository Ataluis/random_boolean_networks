PROG = main
CC = g++
CPPFLAGS = -g -Wall -std=c++17 -fopenmp -O3
OBJS = boolnet.o altnet.o main.o
$(PROG) : $(OBJS)
	$(CC) $(CPPFLAGS) -o $(PROG) $(OBJS)
main.o :
	$(CC) $(CPPFLAGS) -c main.cpp
boolnet.o : boolnet.hpp
	$(CC) $(CPPFLAGS) -c boolnet.cpp
altnet.o : altnet.hpp
	$(CC) $(CPPFLAGS) -c altnet.cpp
clean:
	rm -f core $(PROG) $(OBJS) 
