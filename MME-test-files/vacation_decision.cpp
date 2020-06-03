/*
 Jackson Harding
 
*/

#include <iomanip>
#include <fstream>
#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	cout << "Enter your daily budget ($): ";
	double budget = 0;
	cin >> budget;
	
	cout << "Enter the duration of your vacation (days): ";
	int days = 0;
	cin >> days;
	
	if (budget < 100) 
	{
	  cout << "John's travel destination is: staycation";  
  }
	else if (days < 8)
	{
	  if (budget > 250)
	  cout << "John's travel destination is: New York City"; 
	  else
	  cout << "John's travel destination is: Toronto"; 
  }
	else if (budget > 250)
	 cout << "John's travel destination is: Hong Kong"; 
	else 
   cout << "John's travel destination is: Vancouver"; 
   
   
	return EXIT_SUCCESS;
}

/*


*/
