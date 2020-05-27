LDFLAGS = -g -std=c++11
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS =
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = numerical_notation_canonical numerical_notation

all:	clean $(ALL_TESTS) $(EXE)
	chmod +x *.py $(EXE)

clean:
	/bin/rm -rf *.o $(EXE)

numerical_notation_canonical: numerical_notation_canonical.cpp
	$(CC) $^ -o $@ $(LDFLAGS) $(CFLAGS)

numerical_notation: numerical_notation.cpp
	$(CC) $^ -o $@ $(LDFLAGS) $(CFLAGS)
