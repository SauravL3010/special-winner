/*
factorial_main.cpp

2017-02-22 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <string>
#include "factorial.h"

using namespace std;

int main(const int argc, const char * argv[])
{
  int input = atoi(argv[1]);

  cout << factorial(input) << endl;

  return 0;
}
