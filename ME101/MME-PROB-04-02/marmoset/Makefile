LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = first_bigger.py second_bigger.py equal.py randomize.py else_if.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = bigger_or_smaller

all:	clean $(ALL_TESTS) bigger_or_smaller
	chmod +x $(ALL_TESTS) bigger_or_smaller

clean:
	/bin/rm -rf *.o $(EXE)

bigger_or_smaller.o: bigger_or_smaller.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
bigger_or_smaller: bigger_or_smaller.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	bigger_or_smaller.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
