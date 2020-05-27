/*
above_or_below.cpp

2018-03-16 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <cstdlib>
#include <cmath>

int main()
{
    const double TOLERANCE = 1e-6;
    std::string position;
    double x_coordinate = 0.0, y_coordinate = 0.0;

    std::cout << "Enter the x,y coordinates for a point: ";
    std::cin >> x_coordinate >> y_coordinate;

    if (std::abs(x_coordinate - y_coordinate) < TOLERANCE)
        position = "on";
    else if (x_coordinate > y_coordinate)
        position = "below";
    else
        position = "above";

    std::cout << "The point is " << position << " the line y=x." << std::endl;
    return 0;
}
