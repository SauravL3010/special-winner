LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = numbers.py one_per_line.py uses_while.py not_for.py not_do_while.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = first_while_loop

all:	clean $(ALL_TESTS) first_while_loop
	chmod +x $(ALL_TESTS) first_while_loop

clean:
	/bin/rm -rf *.o $(EXE)

first_while_loop.o: first_while_loop.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
first_while_loop: first_while_loop.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	first_while_loop.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
