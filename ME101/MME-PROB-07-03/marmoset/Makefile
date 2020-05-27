LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = console_output.py sample_input.py constant_input.py num_lines.py randomize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = coordinate_tracking

all:	clean $(ALL_TESTS) coordinate_tracking
	chmod +x $(ALL_TESTS) coordinate_tracking

clean:
	/bin/rm -rf *.o $(EXE)

coordinate_tracking.o: coordinate_tracking.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
coordinate_tracking: coordinate_tracking.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	coordinate_tracking.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
