LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = 10_toonie.py 20_dime.py 30_treefiddy.py 40_round_down.py 50_round_up.py 60_every_coin.py 70_max_amount.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = making_change

all:	clean $(ALL_TESTS) making_change
	chmod +x $(ALL_TESTS) making_change

clean:
	/bin/rm -rf *.o $(EXE)

making_change.o: making_change.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
making_change: making_change.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	making_change.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
