//Builds a set of directions and distances for file3
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	ifstream fin("file3.txt");
    double theta = 0, totTheta = 0, x = 0, y = 0, dist = 0, totDist = 0;
    while(fin >> theta >> dist)
    {
    	//we want to make sure we are within 0 to 360
    	totTheta = fmod(totTheta + theta, 360.0);
    	
    	double radTheta = totTheta * M_PI / 180.0; 
    	
    	x = x + dist*cos(radTheta);
    	y = y + dist*sin(radTheta);
    	
    	totDist += dist;
    }
    
    cout << "Total distance: " << totDist << "m" <<  endl;
    cout << "(x,y) = (" << x << "," << y << ")" << endl;
    cout << "Orientation: " << totTheta << " Degrees";
}
















