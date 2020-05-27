all: clean permissions balance_1

clean:
	rm -rf *.o balance_1

permissions:
	chmod +x $(wildcard *.py)

balance_1: balance_1.cpp
	g++ -std=c++11 balance_1.cpp -o balance_1
	chmod +x balance_1
