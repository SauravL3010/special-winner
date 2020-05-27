/*
time_of_flight.cpp

2018-04-07 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double velocity = 0.0;
    double angle_deg = 0.0;
    double elevation = 0.0;
    double time_1 = 0.0, time_2 = 0.0;

    cout << "Enter the launch velocity [m/s] : ";
    cin >> velocity;
    cout << "Enter the launch angle [degrees] : ";
    cin >> angle_deg;
    cout << "Enter the change in elevation from launch to landing [m] : ";
    cin >> elevation;

    double angle_rad = angle_deg * M_PI / 180;
    time_1 = -10.0/981 * (sqrt(2)*sqrt(50*pow(velocity,2)*pow(sin(angle_rad),2)-981*elevation)
                          - 10 * velocity * sin(angle_rad));
    time_2 = 10.0/981 * (sqrt(2)*sqrt(50*pow(velocity,2)*pow(sin(angle_rad),2)-981*elevation)
                          + 10 * velocity * sin(angle_rad));
                          
    cout << "The first calculated time of flight is: " << time_1 << " seconds." << endl;
    cout << "The second calculated time of flight is: " << time_2 << " seconds." << endl;

    return 0;
}
