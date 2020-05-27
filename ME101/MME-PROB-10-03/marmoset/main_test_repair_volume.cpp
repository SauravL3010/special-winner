/*
main_test_volume_repair.cpp

substitute main() function for testing volume_repair() function

© 2019 DAVID LAU ALL RIGHTS RESERVED
*/

#define MARMOSET_TESTING

#include <fstream>
#include <iostream>
#include <iomanip>
#include "filling_potholes.cpp"

namespace canonical
{
  const int QTY_STREET = 75;
  const int QTY_AVENUE = 75;

  void read_file(std::ifstream & fin, int pothole_map[canonical::QTY_STREET][canonical::QTY_AVENUE]);

}


int main(int argc, char * argv[])
{
  std::ifstream fin("potholes.txt");

  if (!fin)
  {
    std::cerr << "Unable to open potholes.txt." << std::endl;
    return -1;
  }

  int pothole_map[canonical::QTY_STREET][canonical::QTY_AVENUE] = {};

  read_file(fin, pothole_map);

  fin.close();

  std::ifstream fin_sequence("test_repair_volume.txt");

  if (!fin_sequence)
  {
    std::cerr << "Unable to open test_repair_volume.txt." << std::endl;
    return -1;
  }

  std::string street_or_avenue;
  int road_number = 0;

  while (fin_sequence >> street_or_avenue >> road_number)
  {
    double function_result = repair_volume(pothole_map, road_number, street_or_avenue == "S");

    std::cout << function_result << std::endl;
  }

  fin_sequence.close();
  return 0;
}


void canonical::read_file(std::ifstream & fin, int pothole_map[canonical::QTY_STREET][canonical::QTY_AVENUE])
{
  int street_num = 0, avenue_num = 0, radius = 0;

  while (fin >> street_num >> avenue_num >> radius)
  {
    pothole_map[street_num - 1][avenue_num - 1] = radius;
  }
}
