LDFLAGS = -g -std=c++11
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = function_declarations.py test_read_file.py test_repair_volume.py next_repair.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = filling_potholes test_read_file test_repair_volume

all:	clean $(ALL_TESTS) test_read_file test_repair_volume filling_potholes
	chmod +x *.py test_read_file test_repair_volume filling_potholes

clean:
	/bin/rm -rf *.o $(EXE)

test_read_file: main_test_read_file.cpp
	$(CC) $^ -o $@ $(LDFLAGS) $(CFLAGS)

test_repair_volume: main_test_repair_volume.cpp
	$(CC) $^ -o $@ $(LDFLAGS) $(CFLAGS)

filling_potholes.o: filling_potholes.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
filling_potholes: filling_potholes.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	filling_potholes.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
