LDFLAGS = -g -std=c++11
CFLAGS = -Wno-write-strings -Wall -g -Werror
CC = g++

PUBLIC_TESTS = test_run_python_01.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE =

all:	clean $(ALL_TESTS)
	chmod +x *.py

clean:
	/bin/rm -rf *.o $(EXE)
