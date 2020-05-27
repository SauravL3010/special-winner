/*
first_do_while.cpp

2018-03-20 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

int main()
{
    int the_sum = 0;
    int first_number = 0;
    int second_number = 0;

    do {
        std::cout << "Enter the first odd positive integer: ";
        std::cin >> first_number;
    } while (first_number <= 0 || first_number % 2 == 0);

    do {
        std::cout << "Enter the second odd positive integer: ";
        std::cin >> second_number;
    } while (second_number <= 0 || second_number % 2 == 0);

    the_sum = first_number + second_number;

    std::cout << "The sum of the entered numbers is " << the_sum << "." << std::endl;
}
