// binary_conversion.cpp
// 2018-09-18 - created
// © 2018 DAVID LAU ALL RIGHTS RESERVED

#include <iostream>

int main()
{
    int decimal_number{0};

    std::cout << "Please enter a decimal number to convert to binary: ";
    std::cin >> decimal_number;

    std::cout << decimal_number / 128;
    decimal_number = decimal_number % 128;
    std::cout << decimal_number / 64;
    decimal_number = decimal_number % 64;
    std::cout << decimal_number / 32;
    decimal_number = decimal_number % 32;
/* if (statement) */
    std::cout << decimal_number / 16;
    decimal_number = decimal_number % 16;
    std::cout << decimal_number / 8;
    decimal_number = decimal_number % 8;
    std::cout << decimal_number / 4;
    decimal_number = decimal_number % 4;
    std::cout << decimal_number / 2;
    decimal_number = decimal_number % 2;
    std::cout << decimal_number << std::endl;

//  this commented code is here to test whether the no_if_statements.py and
//  no_loops.py tests falsely flag code within comments
//  if (statement)
//  {
//  }
//  while (statement)
//  {
//  }
//  for (statement; statement; statement)
//  {
//  }
//  do {
//  } while (statement);
/*
if (statement)
{
    fake end of comment
    * /
}
while (statement)
{
}
*/
/*
for (statement; statement; statement)
{
}
do {
} while (statement);
*/

    return 0;
}
