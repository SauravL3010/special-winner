//Builds a set of directions and distances for file3
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	ifstream fin("file4.txt");
	ofstream fout("salesFile.txt");
	string prodName = "";
	double cost = 0, preTaxTotal = 0, savings = 0;
	bool isSale = 0;
	int discount = 0;
	while(fin >> prodName >> cost >> isSale)
	{
		discount = 0; //I need to reset this, since it gets set if the
		//previous product is on sale
		double price = cost; //this is adjusted if there is a discount
		if(isSale == 1)
		{
			fin >> discount; //obtain the discount
		}
		price = price * (1-discount/100.0); //apply the discount
		savings += cost*(discount/100.0); //compute the savings
		preTaxTotal += price;
	}
	fout << fixed << setprecision(2); //this works in an output file stream, too
	fout << "The pre-tax total is: $" << preTaxTotal << endl;
	//I didn't give you an amount for tax, so you can make it up if you want
	fout << "The post-tax total is: $" << preTaxTotal*1.13 << endl;
	fout << "You saved: $" << savings << endl;
}
















