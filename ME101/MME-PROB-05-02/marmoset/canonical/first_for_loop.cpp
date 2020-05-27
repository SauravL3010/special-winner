/*
first_for_loop.cpp

2018-02-22 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int loop_limit = 0;

    cout << "Enter a positive integer: ";
    cin >> loop_limit;

    for (int print_number = 1; print_number <= loop_limit; print_number++)
        cout << print_number << endl;

    return EXIT_SUCCESS;
}
