LDFLAGS = -g
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = sample_data.py max_size.py min_size.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = secret_message

all:	clean $(ALL_TESTS) secret_message
	chmod +x $(ALL_TESTS) secret_message

clean:
	/bin/rm -rf *.o $(EXE)

secret_message.o: secret_message.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
secret_message: secret_message.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	secret_message.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
