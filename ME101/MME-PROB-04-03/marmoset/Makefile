LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = above.py below.py on_exact.py on_tolerance.py randomize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = above_or_below

all:	clean $(ALL_TESTS) above_or_below
	chmod +x $(ALL_TESTS) above_or_below

clean:
	/bin/rm -rf *.o $(EXE)

above_or_below.o: above_or_below.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
above_or_below: above_or_below.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	above_or_below.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
