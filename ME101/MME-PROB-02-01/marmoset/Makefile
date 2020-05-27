LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = prompt.py single_digit_int.py three_digit_int.py negative_int.py float.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = read_and_print

all:	clean $(ALL_TESTS) read_and_print
	chmod +x $(ALL_TESTS) read_and_print

clean:
	/bin/rm -rf *.o $(EXE)

read_and_print.o: read_and_print.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
read_and_print: read_and_print.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	read_and_print.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
