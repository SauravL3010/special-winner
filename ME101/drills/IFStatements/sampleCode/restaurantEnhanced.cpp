#include <iostream>
using namespace std;

int main()
{
	double preTaxAmount = 0.0;
	cout << "Enter the pre-tax amount";
	cin >> preTaxAmount;
	
	double finalAmount = preTaxAmount;
	
	if(preTaxAmount < 0)
	{
		cout << "Negative amounts not allowed!";
		return 0; //don't let anything else happen, just exit
	}
	else if(preTaxAmount > 10)
	{
		finalAmount = preTaxAmount * 1.13;
	}
	else if(preTaxAmount > 5)
	{
		finalAmount = preTaxAmount * 1.07;
	}
	
	/*
		Did you notice that I didn't check for the case between 0 and 
		5?  This is already handled when I declare finalAmount to be
		equal to preTaxAmount.  Since I don't need to change anything
		for this case, I didn't consider it.  If you did consider it,
		that's usually OK.  It just makes the code slightly longer.
	*/
	
	//We didn't tell you to output, but we might as well
	cout << "The final amount is: " << finalAmount;
	return 0;
}
