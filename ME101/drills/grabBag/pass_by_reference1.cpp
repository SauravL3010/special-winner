#include <iostream>
using namespace std;

int twoDArray(int ar[][5])
{
	return 4;
}

void swapOne(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;
}

void swapTwo(int &a, int &b)
{
	int temp = a;
	a = b;
	b = temp;
}

int main()
{
	int AR[3][5];
	twoDArray(AR);
	int a = 4, b = 3;
	swapOne(a,b);
	cout << a << " " << b << endl;
	swapTwo(a,b);
	cout << a << " " << b << endl;
}
