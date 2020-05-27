#include <iostream>

using namespace std;

int main()
{
  int SDS = 0;
  string product_identifier[4];
  int carcinogenity = 0;
  int reproductive_toxicity = 0;
  int STOT_repeat_exposure = 0;
  double composition_iron = 0.0;
  double composition_manganese = 0.0;
  double composition_chromium = 0.0;
  double composition_nickel = 0.0;

  cout << "SDS ID No.: ";
  cin >> SDS;

  cout << "Product Identifier: ";
  for (int word_num = 0; word_num < 4; word_num++)
    cin >> product_identifier[word_num];

  cout << "Carcinogenity: ";
  cin >> carcinogenity;

  cout << "Reproductive Toxicity: ";
  cin >> reproductive_toxicity;

  cout << "STOT Repeat Exposure: ";
  cin >> STOT_repeat_exposure;

  cout << "Composition (% weight):" << endl;
  cout << "Iron: ";
  cin >> composition_iron;

  cout << "Manganese: ";
  cin >> composition_manganese;

  cout << "Chromium: ";
  cin >> composition_chromium;

  cout << "Nickel: ";
  cin >> composition_nickel;

  cout << endl;
  cout << "SDS: " << SDS << "     Identifier: ";
  for (int word_num = 0; word_num < 4; word_num++)
    cout << product_identifier[word_num] << " ";
  cout << endl;

  cout << "Hazard: "
       << carcinogenity << "-"
       << reproductive_toxicity << "-"
       << STOT_repeat_exposure << endl;

  cout << "Composition:" << endl;
  cout << "Fe    Mn    Cr    Ni" << endl;
  cout << composition_iron << "    "
       << composition_manganese << " "
       << composition_chromium << "  "
       << composition_nickel << endl;

  return 0;
}
