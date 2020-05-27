LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = prompt.py first_number.py last_number.py quantity_of_numbers.py all_numbers_match.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = counting_up

all:	clean $(ALL_TESTS) counting_up
	chmod +x $(ALL_TESTS) counting_up

clean:
	/bin/rm -rf *.o $(EXE)

counting_up.o: counting_up.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
counting_up: counting_up.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	counting_up.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
