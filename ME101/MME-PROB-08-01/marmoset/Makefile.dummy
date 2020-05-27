LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = check_filename.py run_Makefile.py run_function.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = dummy

all:	clean $(ALL_TESTS) dummy
	chmod +x $(ALL_TESTS) dummy

clean:
	/bin/rm -rf *.o $(EXE)

dummy.o: dummy.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
dummy: dummy.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	dummy.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
