/*
© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  double input_number = 0.0;

  cout << "Enter the number to re-format: ";
  cin >> input_number;

  cout << endl;
  cout << input_number << endl;
  cout << setprecision(2);
  cout << input_number << endl;
  cout << setprecision(16);
  cout << input_number << endl;
  cout << fixed << setprecision(6);
  cout << input_number << endl;
  cout << fixed << setprecision(0);
  cout << input_number << endl;
  cout << scientific << setprecision(8);
  cout << input_number << endl;

  return 0;
}
