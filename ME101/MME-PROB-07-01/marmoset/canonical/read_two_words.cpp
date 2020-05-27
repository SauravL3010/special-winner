/*
read_two_words.cpp

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream file_in("two_words.txt");
  string words[2];

  file_in >> words[0] >> words[1];

  cout << words[0] << " " << words[1] << endl;

  file_in.close();
  return 0;
}
