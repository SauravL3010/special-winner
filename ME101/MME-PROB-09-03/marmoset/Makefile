LDFLAGS = -g -std=c++11
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = gen_catalog.py gen_BOMs.py output_file_exists.py output_text.py design_names.py part_descriptions.py design_costs.py summary.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = request_for_quote

all:	clean $(ALL_TESTS) request_for_quote
	chmod +x $(ALL_TESTS) request_for_quote

clean:
	/bin/rm -rf *.o $(EXE)

request_for_quote.o: request_for_quote.cpp
	$(CC) -c $(LDFLAGS) $<

# g++ <$^:all prereqs> -o <$@:target> <flags>
request_for_quote: request_for_quote.o
	$(CC) $^ -o $@ $(CFLAGS)

check:	request_for_quote.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"
