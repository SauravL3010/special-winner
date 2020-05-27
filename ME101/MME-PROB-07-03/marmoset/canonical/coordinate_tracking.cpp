/*
coordinate_tracking.cpp

2018-02-22 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin("drone_directions.txt");

    double instruct_distance = 0.0;
    double instruct_heading = 0.0;
    double x_coordinate = 0.0;
    double y_coordinate = 0.0;
    double last_heading = 0.0;

    while (fin >> instruct_distance >> instruct_heading)
    {
        double current_heading = last_heading + instruct_heading;
        x_coordinate = x_coordinate + instruct_distance * cos(current_heading * M_PI / 180);
        y_coordinate = y_coordinate + instruct_distance * sin(current_heading * M_PI / 180);
        cout << "(" << x_coordinate << "," << y_coordinate << ")" << endl;
        last_heading = current_heading;
    }

    fin.close();
    return EXIT_SUCCESS;
}
