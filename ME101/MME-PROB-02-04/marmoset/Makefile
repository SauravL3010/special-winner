LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = description_sample_input_fields.py description_sample_output_values.py output_full_match.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)


EXE = steel_MSDS

all:	clean $(ALL_TESTS) steel_MSDS
	chmod +x $(ALL_TESTS) steel_MSDS

clean:
	/bin/rm -rf *.o $(EXE)

steel_MSDS.o: steel_MSDS.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
steel_MSDS: steel_MSDS.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	steel_MSDS.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
