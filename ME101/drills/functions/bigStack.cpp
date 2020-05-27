#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int arSize = pow(2,21) - 1024*24;
	char c[arSize];
	for(int i = 0; i < arSize; i++)
	{
		if(i%1000 == 0)
		{
			c[i] = 'a';
			cout << i << " " << c[i] << endl;
			}
	}
}
