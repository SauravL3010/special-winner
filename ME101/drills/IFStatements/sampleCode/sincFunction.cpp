#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	double x = 0.0;
	cin >> x;
	
	/*
		I have two ways (at least...) to do this.  I will demonstrate
		both below.  In the first, I use only a single if statement, 
		and I initialize the variable f_x to 1.  This avoids checking
		if x == 0, but also makes my code a bit less clear 
	*/
	double f_x = 1;
	if(x != 0)
	{
		f_x = sin(x)/x;
	}
	
	//here is the second way.  It's commented, so it won't run until
	//you uncomment.
	
	/*
	if(x == 0)
	{
		//it's a bit more clear that I have a special case for value
		//x = 0.
		f_x = 1;
	}
	else
	{
		f_x = sin(x)/x'
	}
	*/
	cout << f_x;
}
