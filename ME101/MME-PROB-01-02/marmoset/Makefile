LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = filesize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = missing_semi-colon

all:	clean $(ALL_TESTS) missing_semi-colon
	chmod +x $(ALL_TESTS) missing_semi-colon

clean:
	/bin/rm -rf *.o $(EXE)

missing_semi-colon.o: missing_semi-colon.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
missing_semi-colon: missing_semi-colon.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	missing_semi-colon.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
