LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_data_1.py sample_data_2.py same_height.py above.py below.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = time_of_flight

all:	clean $(ALL_TESTS) time_of_flight
	chmod +x $(ALL_TESTS) time_of_flight

clean:
	/bin/rm -rf *.o $(EXE)

time_of_flight.o: time_of_flight.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
time_of_flight: time_of_flight.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	time_of_flight.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
