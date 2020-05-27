/*
bigger_or_smaller.cpp

2018-02-22 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

using namespace std;

int main()
{
    int num1 = 0, num2 = 0;

    cout << "Enter two integers: ";
    cin >> num1 >> num2;

    if (num1 > num2)
        cout << "The first number is larger." << endl;
    else if (num2 > num1)
        cout << "The second number is larger." << endl;
    else
        cout << "The two numbers are equal." << endl;

    return 0;
}
