/*
even_or_odd.cpp

2018-02-08 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

using namespace std;

int main()
{
  int input_integer = 0;

  cout << "Enter a positive integer: ";
  cin >> input_integer;
  cout << endl;

  cout << "The number that you entered is ";
  if (input_integer % 2 == 0)
    cout << "even." << endl;
  else
    cout << "odd." << endl;

  return 0;
}
