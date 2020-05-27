Problem Number: MME-PROB-03-01
------------------------------

Problem Title: Numerical Notation
==================================

Code filename: numerical_notation.cpp

Write a program that inputs a floating point number with at least double precision (~15 digits). Output this number in the following forms:

* default cout format (6 digits of precision)
* 2 digits of precision
* 16 digits of precision
* fixed notation with 6 decimal digits of precision
* fixed notation with 0 decimal digits of precision
* scientific notation with 8 digits of precision

You will likely require the use of the <iostream> and <iomanip> libraries for this program. You may start with the following program skeleton.

    #include <iostream>
    #include <iomanip>

    using namespace std;

    int main()
    {

      return 0;
    }

### Sample Input

    Enter the number to re-format: 299792458

### Sample Output

    2.99792e+08
    3e+08
    299792458
    299792458.000000
    299792458
    2.99792458e+08


© 2017 DAVID LAU ALL RIGHTS RESERVED
