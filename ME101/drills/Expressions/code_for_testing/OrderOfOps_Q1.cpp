#include <iostream>
#include <cmath> //needed for certain functions
using namespace std;
int main()
{
	double a,b,c,d,e;
	cout << "Enter the five numbers: ";
	cin >> a >> b >> c >> d >> e;
	double x, y, z;
	x = pow(b,2.0) + pow(c,5.0) + pow(d,2.0)/3;
	y = a + b/2*8 + 90;
	z = 3*a + 4*b + 5*c;
	cout << "X: " << x << " Y: " << y << " Z: " << z;
}
