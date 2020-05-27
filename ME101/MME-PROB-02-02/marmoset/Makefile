LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = prompts.py colons.py radius_conversion.py integer_radius.py float_radius.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = sphere_calculations

all:	clean $(ALL_TESTS) sphere_calculations
	chmod +x $(ALL_TESTS) sphere_calculations

clean:
	/bin/rm -rf *.o $(EXE)

sphere_calculations.o: sphere_calculations.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
sphere_calculations: sphere_calculations.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	sphere_calculations.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
