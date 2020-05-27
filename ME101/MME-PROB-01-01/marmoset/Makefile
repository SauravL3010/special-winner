LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = filename.py two_words_match.py single_space.py case_sensitive.py exclamation.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = hello_world

all:	clean $(ALL_TESTS) hello_world
	chmod +x $(ALL_TESTS) hello_world

clean:
	/bin/rm -rf *.o $(EXE)

hello_world.o: hello_world.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
hello_world: hello_world.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	hello_world.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
