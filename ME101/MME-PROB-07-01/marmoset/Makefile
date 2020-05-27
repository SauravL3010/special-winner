LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = description_sample.py different_words.py check_spacing.py words_separated.py single_line.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = read_two_words

all:	clean $(ALL_TESTS) read_two_words
	chmod +x $(ALL_TESTS) read_two_words

clean:
	/bin/rm -rf *.o $(EXE)

read_two_words.o: read_two_words.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
read_two_words: read_two_words.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	read_two_words.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
