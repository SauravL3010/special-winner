LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = all_valid.py first_entry_even.py first_entry_negative.py many_invalids.py uses_do_while.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = first_do_while

all:	clean $(ALL_TESTS) first_do_while
	chmod +x $(ALL_TESTS) first_do_while

clean:
	/bin/rm -rf *.o $(EXE)

first_do_while.o: first_do_while.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
first_do_while: first_do_while.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	first_do_while.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
