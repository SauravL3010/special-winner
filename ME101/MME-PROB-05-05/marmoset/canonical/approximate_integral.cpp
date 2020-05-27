/*
approximate_integral.cpp

2018-04-12 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    double step_size = 0.0;
    double integral_sum = 0.0;
    double f_x = 0.0;

    cout << "Enter the step size for calculating the definite integral: ";
    cin >> step_size;

    for (double x_val = 3.1; x_val <= 17.9; x_val += step_size)
    {
        f_x = sin(log(2*pow(x_val,3)-5*pow(x_val,2)+sqrt(3*x_val)+2))/(8*pow(x_val,2));
        integral_sum += f_x * step_size;
    }
    cout << setprecision(14);
    cout << integral_sum << endl;

    return 0;
}
