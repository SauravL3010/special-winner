LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = count_lines.py array_1.py array_2.py array_3.py not_hard_coded.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = 2D_print

all:	clean $(ALL_TESTS) 2D_print
	chmod +x $(ALL_TESTS) 2D_print

clean:
	/bin/rm -rf *.o $(EXE)

2D_print.o: 2D_print.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
2D_print: 2D_print.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	2D_print.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
