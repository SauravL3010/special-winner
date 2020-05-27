LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = low_numbers.py one_per_line.py uses_for.py not_while.py single.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = first_for_loop

all:	clean $(ALL_TESTS) first_for_loop
	chmod +x $(ALL_TESTS) first_for_loop

clean:
	/bin/rm -rf *.o $(EXE)

first_for_loop.o: first_for_loop.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
first_for_loop: first_for_loop.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	first_for_loop.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
