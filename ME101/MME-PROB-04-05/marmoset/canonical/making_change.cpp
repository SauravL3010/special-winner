#include <iostream>
#include <cstdlib>

int main()
{
  int qty_dollars = 0;
  int qty_cents = 0;
  int qty_coins = 0;

  std::cout << "Enter the number of dollars:" << std::endl;
  std::cin >> qty_dollars;

  std::cout << "Enter the number of cents:" << std::endl;
  std::cin >> qty_cents;

  int total_cents = qty_dollars * 100 + qty_cents;

  if (total_cents % 5 >= 3)
    total_cents = total_cents + (5 - (total_cents % 5));

  int qty_toonies = total_cents / 200;
  total_cents = total_cents % 200;
  int qty_loonies = total_cents / 100;
  total_cents = total_cents % 100;
  int qty_quarters = total_cents / 25;
  total_cents = total_cents % 25;
  int qty_dimes = total_cents / 10;
  total_cents = total_cents % 10;
  int qty_nickels = total_cents / 5;
  total_cents = total_cents % 5;

  qty_coins = qty_toonies + qty_loonies + qty_quarters + qty_dimes + qty_nickels;

  std::cout << "Minimum number of coins needed:" << std::endl;
  std::cout << qty_coins << std::endl;

  return EXIT_SUCCESS;
}
