#include <iostream>
#include <cstdlib>
#include <cmath>

int main()
{
  int num_to_check {0};
  bool is_prime = true;

  std::cout << "Enter the number to check if prime: ";
  std::cin >> num_to_check;

  for (int check_factor = 2; check_factor <= sqrt(num_to_check); check_factor++)
  {
    if (num_to_check % check_factor == 0)
      is_prime = false;
  }

  if (is_prime)
    std::cout << "The number is a prime number." << std::endl;
  else
    std::cout << "The number is a composite number." << std::endl;

  return EXIT_SUCCESS;
}
