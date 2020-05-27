LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_input.py reordered_sample.py subset_sample.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = medal_count

all:	clean $(ALL_TESTS) medal_count
	chmod +x $(ALL_TESTS) medal_count

clean:
	/bin/rm -rf *.o $(EXE)

coordinate_tracking.o: medal_count.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
coordinate_tracking: medal_count.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	medal_count.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
