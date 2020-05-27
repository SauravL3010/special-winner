//Builds a set of directions and distances for file3
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	ifstream fin("file2.txt");
    int numEntries = 0;
    int i = 0;
    while(fin >> numEntries)
    {
    	int temp = 0;
    	int sum = 0; //initialize INSIDE the while loop!
    	for(int i = 0; i < numEntries; i++)
    	{
    		fin >> temp;
    		sum += temp;
    	}
    	if(i == 0)
    	{
    		cout << sum << endl;
    		i++;
    	}
    }
}
















