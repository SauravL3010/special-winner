/*
TEMPLATE FILE: time_of_flight.cpp
*/

#include <iostream>

using namespace std;

const double G_EARTH = 9.80665;   // meters per second squared

double time_of_flight(double initial_velocity)
{
  /* insert code here */
}

int main()
{
  double initial_velocity = 0.0;

  do {
    cout << "Enter the initial velocity (m/s): ";
    cin >> initial_velocity;
  } while(initial_velocity <= 0);

  cout << "The projectile will return to the ground in "
       << time_of_flight(initial_velocity) << " seconds." << endl;

  return 0;
}
