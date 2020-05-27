/*
2D_print.cpp

2018-04-04 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <iomanip>

using namespace std;

const int A1_ROWS = 3;
const int A1_COLS = 2;

const int A2_ROWS = 5;
const int A2_COLS = 7;

const int A3_ROWS = 3;
const int A3_COLS = 3;

int main()
{
    int array_1[A1_ROWS][A1_COLS] =
    {   {5, 3},
        {2, 2},
        {1, 7}};

    double array_2[A2_ROWS][A2_COLS] =
    {   {3.2, -1.7, 3.6, 1.2, -0.6, 8.0, -7.7},
        {-0.8, 1.1, 2.3, 2.3, -4.8, 8.0, -1.2},
        {1.2, 3.3, 6.8, -2.1, 0.0, 2.3, -8.0},
        {4.2, 5.7, 3.3, -9.0, -8.0, -3.3, 2.2},
        {0.9, 5.7, 3.2, -8.9, 8.0, -8.0, -7.7}};

    string array_3[A3_ROWS][A3_COLS] =
    {   {"Mike", "Carol", "Ryan"},
        {"David", "Fiona", "Chris"},
        {"Pete", "June", "Don"}};

    for (int row = 0; row < A1_ROWS; row++)
    {
        for (int col = 0; col < A1_COLS; col++)
        {
            cout << setw(5) << array_1[row][col];
        }
        cout << endl;
    }
    cout << endl;

    for (int row = 0; row < A2_ROWS; row++)
    {
        for (int col = 0; col < A2_COLS; col++)
        {
            cout << setw(7) << array_2[row][col];
        }
        cout << endl;
    }
    cout << endl;

    for (int row = 0; row < A3_ROWS; row++)
    {
        for (int col = 0; col < A3_COLS; col++)
        {
            cout << setw(7) << array_3[row][col];
        }
        cout << endl;
    }
    cout << endl;

    return 0;
}
