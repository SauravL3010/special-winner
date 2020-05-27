#include <iostream>
using namespace std;
int getNumberLines()
{
	int retVal = 0;
	while(retVal <= 0)
	{
		cout << "How many lines do you want to see?";
		cin >> retVal;
	}
	return retVal;
}

char getDesiredChar()
{
	char retVal = 'x'; //Arbitrary initialization
	cout << "Which character do you want to see?";
	cin >> retVal; //I don't need to validate this one
	return retVal;
}


/*
These next two functions will seem sort of useless.   They are here because they
allow us to talk about the algorithm in terms like "Print out spaces", rather
than "cout << " " ".

Notice that they are void because they do not return anything, they are purely
display functions
*/
void printSpace()
{
	cout << " ";
}
void printSingleChar(char c)
{
	cout << c;
}

void printSpaceRow(int nSpaces)
{
	for(int i = 0; i < nSpaces; i++)
	{
		printSpace(); //call the function if you have it, do NOT duplicate
		//functionality
	}
}

void printCharRow(char c, int nChars)
{
	for(int i = 0; i < nChars; i++)
	{
		printSingleChar(c); //again, call the function
	}
}

//primarily, we will be printing rows in the pyramid, so why not write this?
void printRow(char c, int nSpaces, int nChars)
{
	printSpaceRow(nSpaces);
	printCharRow(c,nChars);
	cout << endl;
}

void printPyramid(char c, int nRows)
{
	for(int i = 0; i < nRows; i++)
	{
		int nSpaces = nRows - i;
		int nChars = 2*i + 1;
		printRow(c,nSpaces,nChars);
	}
}

int main()
{
	int nRows = getNumberLines();
	char c = getDesiredChar();
	printPyramid(c,nRows);
}















