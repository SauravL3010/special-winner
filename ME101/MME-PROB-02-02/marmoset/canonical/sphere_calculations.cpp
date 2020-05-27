/*
sphere_calculations.cpp

2017-03-10 - created
2018-04-10 - updated: removed convertUnits function, fixed area calculation

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Radius
{
private:
  static const float YARDS_TO_METERS;
  double dimension;
  string base_units;
public:
  Radius()
  {
    dimension = 0.0;
    base_units = "METERS";
  }
  double getDimension(string get_units)
  {
      if (get_units != "METERS" && get_units != "YARDS")
        throw 1;

      double converted_dimension = dimension;
      if (get_units != base_units)
      {
          if (base_units == "YARDS" && get_units == "METERS")
            converted_dimension = converted_dimension * YARDS_TO_METERS;
          else if (base_units == "METERS" && get_units == "YARDS")
            converted_dimension = converted_dimension / YARDS_TO_METERS;
      }

      return converted_dimension;
  }
  void setRadius(double set_dimension, string set_units)
  {
    if (set_units == "METERS" || set_units == "YARDS")
    {
      base_units = set_units;
      dimension = set_dimension;
    }
    else
    {
      throw 1;
    }
  }
  void operator = (const Radius & assign)
  {
    dimension = assign.dimension;
    base_units = assign.base_units;
  }
};

const float Radius::YARDS_TO_METERS = 0.9144;

class Sphere
{
private:
public:
  Radius radius;
  double getSurfaceArea(string base_units)
  {
    return 4 * M_PI * pow(radius.getDimension(base_units),2);
  }
  double getVolume(string base_units)
  {
    return 4.0/3 * M_PI * pow(radius.getDimension(base_units),3);
  }
};

int main()
{
  try
  {
    double in_radius = 0.0;
    Sphere sphere1, sphere2;

    cout << "Enter the radius of sphere 1 in yards: ";
    cin >> in_radius;

    sphere1.radius.setRadius(in_radius, "YARDS");

    cout << "Enter the radius of sphere 2 in yards: ";
    cin >> in_radius;

    sphere2.radius.setRadius(in_radius, "YARDS");

    cout << endl;
    cout << setw(45) << "*Sphere 1*" << setw(20) << "*Sphere 2*" << endl;
    cout << setw(25) << "radius [m] : ";
    cout << setw(20) << sphere1.radius.getDimension("METERS");
    cout << setw(20) << sphere2.radius.getDimension("METERS") << endl;
    cout << setw(25) << "surface area [m^2] : ";
    cout << setw(20) << sphere1.getSurfaceArea("METERS");
    cout << setw(20) << sphere2.getSurfaceArea("METERS") << endl;
    cout << setw(25) << "volume [m^3] : ";
    cout << setw(20) << sphere1.getVolume("METERS");
    cout << setw(20) << sphere2.getVolume("METERS") << endl;
  }
  catch (int e)
  {
    if (e == 1)
    {
      cerr << "Exception: invalid units" << endl;
    }
  }


  return 0;
}
