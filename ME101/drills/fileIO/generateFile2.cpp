//Daybuilder: builds days for the meal plan
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>

using namespace std;


int main()
{
	ofstream fout("file2.txt");
	srand(time(NULL));
	for(int i = 0; i < 10000; i++)
	{
		int numEntries = rand()%100 + 1;
		fout << numEntries << endl;
		for(int j = 0; j < numEntries; j++)
		{
			int entry = rand()%637;
			fout << entry << " ";
		}
		fout << endl;
	}
}
















