PROBLEM DESCRIPTION
-------------------
Problem Number: MME-PROB-08-01
------------------------------

Problem Title: Time of Flight Function
======================================

Code filename: time_of_flight.cpp

Complete the function time_of_flight() that calculates the time it takes for a projectile to return to its original position. The projectile launches vertically with an initial velocity.

Use the following code to start. All that is needed is the implementation of the time_of_flight() function. No other code should be modified.

    #include <iostream>

    using namespace std;

    // meters per second squared
    const double G_EARTH = 9.80665;   

    double time_of_flight(double initial_velocity)
    {
      /* write function code here */
    }

    int main()
    {
      double initial_velocity = 0.0;

      do {
        cout << "Enter the initial velocity (m/s): ";
        cin >> initial_velocity;
      } while(initial_velocity <= 0);

      cout << "The projectile will return to the ground in "
           << time_of_flight(initial_velocity) << " seconds."
           << endl;

      return 0;
    }

The time of flight can be calculated as:

<p class="Code">
    time = 2 * initial_velocity / G_EARTH;
</p>

© 2017 DAVID LAU ALL RIGHTS RESERVED
