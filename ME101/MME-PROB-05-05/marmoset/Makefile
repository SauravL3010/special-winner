LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_data_1.py sample_data_2.py large_step.py small_step.py randomize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = approximate_integral

all:	clean $(ALL_TESTS) approximate_integral
	chmod +x $(ALL_TESTS) approximate_integral

clean:
	/bin/rm -rf *.o $(EXE)

approximate_integral.o: approximate_integral.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
approximate_integral: approximate_integral.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	approximate_integral.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
