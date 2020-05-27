/*
main_test_read_file.cpp

substitute main() function for testing read_file() function

© 2019 DAVID LAU ALL RIGHTS RESERVED
*/

#define MARMOSET_TESTING

#include <fstream>
#include <iostream>
#include <iomanip>
#include "filling_potholes.cpp"

int main()
{
    const int QTY_STREET = 75;
    const int QTY_AVE = 75;
    int pothole_map[QTY_STREET][QTY_AVE] = {};

    std::ifstream fin("potholes_read_file.txt");

    read_file(fin, pothole_map);

    for (int street_num = 1; street_num <= QTY_STREET; street_num++)
    {
        for (int avenue_num = 1; avenue_num <= QTY_AVE; avenue_num++)
        {
            if (pothole_map[street_num - 1][avenue_num - 1] > 0)
            {
                std::cout << std::setw(5) << street_num
                          << std::setw(5) << avenue_num
                          << std::setw(10) << pothole_map[street_num - 1][avenue_num - 1]
                          << std::endl;
            }
        }
    }

    return 0;
}
