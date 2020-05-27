/*
finding_slope.cpp

2018-02-27 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

const int NUM_DATA = 1000;

void read_elevations(ifstream & fin, float elevations[NUM_DATA])
{
    for (int data_num = 0; data_num < 1000; data_num++)
    {
        fin >> elevations[data_num];
    }
}

int main()
{
    ifstream fin("trail_elevations.txt");

    float elevations[NUM_DATA] = {0};

    float before_slope = 0.0;
    float after_slope = 0.0;

    int trail_point = 0;

    read_elevations(fin, elevations);

    cout << "Enter the distance (in meters) along the trail where" << endl;
    cout << "you would like to find the slope (between 1 and 998 meters): ";
    cin >> trail_point;

    before_slope = elevations[trail_point] - elevations[trail_point - 1];
    after_slope = elevations[trail_point + 1] - elevations[trail_point];

    cout << fixed << setprecision(1);
    cout << "The slope before the given point is " << before_slope << endl;
    cout << "The slope after the given point is " << after_slope << endl;

    fin.close();

    return EXIT_SUCCESS;
}
