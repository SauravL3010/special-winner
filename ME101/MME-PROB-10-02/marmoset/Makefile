LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_data.py square.py max_size.py min_size.py randomize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = transpose_matrix

all:	clean $(ALL_TESTS) transpose_matrix
	chmod +x $(ALL_TESTS) transpose_matrix

clean:
	/bin/rm -rf *.o $(EXE)

transpose_matrix.o: transpose_matrix.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
transpose_matrix: transpose_matrix.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	transpose_matrix.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
