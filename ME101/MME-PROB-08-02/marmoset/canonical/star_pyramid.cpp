/*
star_pyramid.cpp

2017-02-23 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

using namespace std;

void output_spaces(int quantity_spaces)
{
  for (int space_num = 0; space_num < quantity_spaces; space_num++)
    cout << " ";
}

void output_stars(int quantity_stars)
{
  for (int star_num = 0; star_num < quantity_stars; star_num++)
    cout << "*";
}

int main()
{
  int pyramid_size = 0;

  cout << "Enter the height of the pyramid: ";
  cin >> pyramid_size;

  cout << "start of output" << endl;

  for (int pyramid_level = pyramid_size; pyramid_level > 0; pyramid_level--)
  {
    output_spaces(pyramid_level - 1);
    output_stars(2*pyramid_size - 2*pyramid_level + 1);
    cout << endl;
  }

  cout << "end of output" << endl;

  return 0;
}
