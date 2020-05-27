LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = console_output.py target_names.py distances.py headings.py randomize.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = coordinates_file_read

all:	clean $(ALL_TESTS) coordinates_file_read
	chmod +x $(ALL_TESTS) coordinates_file_read

clean:
	/bin/rm -rf *.o $(EXE)

coordinates_file_read.o: coordinates_file_read.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
coordinates_file_read: coordinates_file_read.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	coordinates_file_read.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
