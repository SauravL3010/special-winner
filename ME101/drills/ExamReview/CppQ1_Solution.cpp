#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	float cash = 0; //cash on hand
	/*
	I need four arrays: one for product names, one for sale price, one for buy
	price, and one for quantity
	*/
	string products[10] = {""};
	float salePrice[10] = {0};
	float buyPrice[10] = {0};
	int quantity[10] = {0};
	
	//open the file for reading
	ifstream fin("inventory.txt");
	//check if it opened
	if(!fin)
	{
		cout << "Could not open file!" << endl;
		return 0; 
	}
	
	//let's read the data in.  
	
	//first, read the cash on hand
	fin >> cash;
	
	//Now, we don't know exactly how many products there are,
	//so we need to use a while loop.
	int i = 0; 
	while(fin >> products[i] >> salePrice[i] >> buyPrice[i] >> quantity[i])
	{
		i++;
		cout << products[i-1] << endl;
	}
	//i now stores the number of products. Note: i is a terrible variable name,
	//but I needed to choose something that would fit on a single printed page
	
	//close the file, or else you can't open it again
	fin.close();
	
	//Time to prompt the user.
	string userChoice = "";
	
	while(userChoice != "STORE_CLOSED")
	{
		//ask the user to enter a product name
		cout << "Enter product name: ";
		cin >> userChoice;
	
		/*
			look for the product.  NOTE: I know that I should check if the user
			entered STORE_CLOSED so that I don't search for it.  Usually, such
			a minor detail is not important on an exam question, so I'll leave
			it out.
		*/
		
		/*
			this is the standard way of searching an array: loop through the 
			array and exit if you find it, or  keep going to the end.
		*/
		bool isFound = false;
		int productIndex = -1;
		for(int j = 0; j < i && !isFound; j++)
		{
			if(products[j] == userChoice)
			{
				isFound = true;
				productIndex = j;
			}
		}
		
		if(isFound == true)
		{
			if(quantity[productIndex] > 0)
			{
				cout << "Enjoy!" << endl;
				//remove it from the inventory
				quantity[productIndex]--;
				//and increase the cash on hand
				cash += salePrice[productIndex];
			}
			else
			{
				cout << "Sorry, we're out of that product." << endl;
			}
		}
		else
		{
			cout << "Sorry, that product doesn't exist." << endl;
		}
	}
	
	/*
		Now the store is closed, so we need to buy things.  I'm going to choose
		to not buy *any* of a product if there is not enough to cash to buy all
		that I need.  You may have chosen something different.
	*/
	for(int j = 0; j < i; j++)
	{
		if(quantity[j] < 10)
		{
			int numNeeded = 10 - quantity[j];
			if(numNeeded*buyPrice[j] < cash)
			{
				cash -= numNeeded * buyPrice[j]; //buy the items
				quantity[j] += numNeeded; //or quantity[j] = 10, either one
			}
		}
	}
	
	//NOW I can output to the file.  All of my transactions for the
	//day are complete.
	ofstream fout("inventory.txt");
	fout << cash << endl;
	for(int j = 0; j < i; j++)
	{
		//now write to the output file
		fout << products[j] << " " << salePrice[j] << " " << buyPrice[j] << " "
			<< quantity[j] << endl;
   }
}
