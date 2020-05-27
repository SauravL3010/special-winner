LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = even.py odd.py random_either.py modulus.py if_else.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = even_or_odd

all:	clean $(ALL_TESTS) even_or_odd
	chmod +x $(ALL_TESTS) even_or_odd

clean:
	/bin/rm -rf *.o $(EXE)

even_or_odd.o: even_or_odd.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
even_or_odd: even_or_odd.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	even_or_odd.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
