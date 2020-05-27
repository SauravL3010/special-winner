LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = 10_323.py 20_11.py 30_1223.py 40_2.py 50_2038074743.py 60_4.py 70_1900002521.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = prime_number

all:	clean $(ALL_TESTS) prime_number
	chmod +x $(ALL_TESTS) prime_number

clean:
	/bin/rm -rf *.o $(EXE)

prime_number.o: prime_number.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
prime_number: prime_number.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	prime_number.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
