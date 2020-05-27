/*
counting_up.cpp

2018-04-02 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

using namespace std;

int main()
{
    int start = 0;
    int end = 0;

    cout << "Counting Up" << endl;
    cout << "Enter the starting integer: ";
    cin >> start;
    cout << "Enter the ending integer: ";
    cin >> end;
    cout << endl;

    for (int current = start; current <= end; current++)
        cout << current << " ";
    cout << endl;

    return 0;
}
