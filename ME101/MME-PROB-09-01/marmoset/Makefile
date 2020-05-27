LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_1.py sample_2.py sample_3.py random_location.py run_5_times.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = finding_slope

all:	clean $(ALL_TESTS) finding_slope canonical_finding_slope
	chmod +x $(ALL_TESTS) finding_slope canonical_finding_slope

clean:
	/bin/rm -rf *.o $(EXE)

finding_slope.o: finding_slope.cpp
	$(CC) -c $(LDFLAGS) $<

canonical_finding_slope.o: canonical_finding_slope.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
finding_slope: finding_slope.o
	$(CC) $^ -o $@ $(CFLAGS)

canonical_finding_slope: canonical_finding_slope.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	finding_slope.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
