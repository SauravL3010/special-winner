LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = 10_staycation1.py 20_staycation2.py 30_staycation3.py 40_Toronto1.py 50_Toronto2.py 60_Vancouver.py 70_NYC1.py 80_NYC2.py 90_HK.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = vacation_decision

all:	clean $(ALL_TESTS) vacation_decision
	chmod +x $(ALL_TESTS) vacation_decision

clean:
	/bin/rm -rf *.o $(EXE)

vacation_decision.o: vacation_decision.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
vacation_decision: vacation_decision.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	vacation_decision.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
