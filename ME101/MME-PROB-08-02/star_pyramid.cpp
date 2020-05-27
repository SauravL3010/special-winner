/*
TEMPLATE FILE: star_pyramid.cpp
*/

#include <iostream>

using namespace std;

void output_spaces(int quantity_spaces)
{
  /* write function code here */
}

void output_stars(int quantity_stars)
{
  /* write function code here */
}

int main()
{
  int pyramid_size = 0;

  cout << "Enter the height of the pyramid: ";
  cin >> pyramid_size;

  for (int pyramid_level = pyramid_size;
       pyramid_level > 0;
       pyramid_level--)
  {
    output_spaces(pyramid_level - 1);
    output_stars(2*pyramid_size - 2*pyramid_level + 1);
    cout << endl;
  }

  return 0;
}
