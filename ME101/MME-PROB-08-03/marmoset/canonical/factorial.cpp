/*
factorial.cpp

2017-02-22 - created

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

long long factorial(const int n)
{
  long long result = 1;

  for (int term = 2; term <= n; term++)
    result = result * term;

  return result;
}
