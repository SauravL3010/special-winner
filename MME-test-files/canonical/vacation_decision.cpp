/*
vacation_decision.cpp

2020-04-22 - created

© 2020 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>

int main()
{
  double daily_budget = 0.0;
  int vacation_duration = 0;

  std::cout << "Enter the daily budget ($): ";
  std::cin >> daily_budget;

  std::cout << "Enter the vacation duration (days): ";
  std::cin >> vacation_duration;

  std::cout << std::endl;
  std::cout << "John's travel destination is: ";

  if (daily_budget < 100)
    std::cout << "staycation" << std::endl;
  else if (vacation_duration < 8)
  {
    if (daily_budget <= 250)
      std::cout << "Toronto" << std::endl;
    else
      std::cout << "New York City" << std::endl;
  }
  else
  {
    if (daily_budget <= 250)
      std::cout << "Vancouver" << std::endl;
    else
      std::cout << "Hong Kong" << std::endl;
  }
  
  return 0;
}
