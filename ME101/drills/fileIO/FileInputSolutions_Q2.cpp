//Builds a set of directions and distances for file3
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	ifstream fin("file1.txt");
    int incoming = 0; //always initialize, even if you are overwriting it!
    while(fin >> incoming)
    {
    	cout << incoming << endl;
    }
}
















