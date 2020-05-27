//Builds a set of directions and distances for file3
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	string s = "file2.txt";
	ofstream fout("file3.txt");
	srand(time(NULL));
	for(int i = 0; i < 20; i++)
	{
		int degs = rand()%90 + 1;
		int dist = rand()%10;
		fout << degs << " " << dist << endl;
	}
}
















