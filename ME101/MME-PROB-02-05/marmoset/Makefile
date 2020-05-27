all: clean permissions binary_conversion

clean:
	rm -rf *.o binary_conversion

permissions:
	chmod +x $(wildcard *.py)

binary_conversion: binary_conversion.cpp
	g++ -std=c++11 binary_conversion.cpp -o binary_conversion
	chmod +x binary_conversion
