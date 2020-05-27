/*
coordinates_file_read.cpp

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    const string INPUT_FILE = "targets.txt";

    ifstream fin(INPUT_FILE.c_str());
    double coordinate_x = 0.0, coordinate_y = 0.0;

    string target_name;
    double distance = 0.0;
    double heading = 0.0;

    while (fin >> target_name >> coordinate_x >> coordinate_y)
    {
        distance = sqrt(coordinate_x * coordinate_x + coordinate_y * coordinate_y);
        heading = atan2(coordinate_y, coordinate_x) * 180/M_PI;
        if (heading < 0)
            heading = heading + 360;
        cout << setprecision(12);
        cout << target_name << " " << distance << " " << heading << endl;
    }

    return 0;
}
