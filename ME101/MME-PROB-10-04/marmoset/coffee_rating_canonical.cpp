/*
coffee_rating.cpp

canonical solution

© 2019 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>

namespace coffee_ratings
{
  const int QTY_INPUT_FILES = 3;

  const int TEMP_MIN = 91;
  const int TEMP_MAX = 99;
  const int TEMP_RANGE = TEMP_MAX-TEMP_MIN+1;

  const int COARSENESS_MIN = 1;
  const int COARSENESS_MAX = 4;
  const int COARSENESS_RANGE = COARSENESS_MAX-COARSENESS_MIN+1;
}

void read_file(std::ifstream & fin, int coffee_ratings[coffee_ratings::TEMP_RANGE][coffee_ratings::COARSENESS_RANGE])
{
  int input_temp = 0;
  int input_coarse = 0;
  int input_rating = 0;

  while (fin >> input_temp >> input_coarse >> input_rating)
  {
    coffee_ratings[input_temp-coffee_ratings::TEMP_MIN][input_coarse-coffee_ratings::COARSENESS_MIN] += input_rating;
  }
}

void best_coffee(int coffee_ratings[coffee_ratings::TEMP_RANGE][coffee_ratings::COARSENESS_RANGE], int & best_temp, int & best_coarseness)
{
  best_temp = coffee_ratings::TEMP_MIN;
  best_coarseness = coffee_ratings::COARSENESS_MIN;

  for (int check_temp = coffee_ratings::TEMP_MIN;
       check_temp <= coffee_ratings::TEMP_MAX;
       check_temp++)
  {
    for (int check_coarseness = coffee_ratings::COARSENESS_MIN;
         check_coarseness <= coffee_ratings::COARSENESS_MAX;
         check_coarseness++)
    {
      if (coffee_ratings[check_temp - coffee_ratings::TEMP_MIN][check_coarseness - coffee_ratings::COARSENESS_MIN] >
        coffee_ratings[best_temp - coffee_ratings::TEMP_MIN][best_coarseness - coffee_ratings::COARSENESS_MIN])
      {
        best_temp = check_temp;
        best_coarseness = check_coarseness;
      }
    }
  }

}

#ifndef MARMOSET_TESTING

int main()
{
  int coffee_ratings[coffee_ratings::TEMP_RANGE][coffee_ratings::COARSENESS_RANGE] = {};

  std::ifstream files_in[coffee_ratings::QTY_INPUT_FILES];
  for (int file_num = 1; file_num <= coffee_ratings::QTY_INPUT_FILES; file_num++)
  {
    std::string filename = "coffee"+std::to_string(file_num)+".txt";
    files_in[file_num - 1].open(filename);

    if (!files_in[file_num - 1])
    {
      std::cerr << "Unable to open " + filename << std::endl;
      return -1;
    }

    read_file(files_in[file_num - 1], coffee_ratings);
    files_in[file_num - 1].close();
  }

  std::ofstream output_file("coffee_rating_canonical.txt");
  int best_temp = 0, best_coarseness = 0;
  best_coffee(coffee_ratings, best_temp, best_coarseness);

  output_file << best_temp << " "
              << best_coarseness << std::endl;

  output_file.close();
  return 0;
}

#endif
