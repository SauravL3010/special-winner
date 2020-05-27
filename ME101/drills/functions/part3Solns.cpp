#include <iostream>
#include <cmath>
using namespace std;

//I need strlen, it's useful
int strlen(char str[])
{
	int i = 0;
	while(str[i] != 0)
		i++;
	//we can return i for the length of the string, or i-1 for the biggest
	//index in the string.  I choose to return i itself.
	return i;
}

//strcmp is actually fairly complicated.  let's consider each case
int strcmp(char str1[], char str2[])
{
	//first, test length
	if(strlen(str1) < strlen(str2))
		return -1;
	
	//Now, we need to test equality. This bit is tricky.  First, notice that
	//we are assured that strlen(str1) >= strlen(str2), so a while loop can be
	//used looking for the end of str2
	int i = 0;
	bool exactlyEqual = 1; 
	while(str2[i] != 0 && exactlyEqual == true)
	{
		if(str1[i] != str2[i])
		{
			exactlyEqual = false;
		}
		i++;
	}
	
	if(exactlyEqual == false)
	{
		//They aren't equal, but which one comes first?
		if(str1[i-1] > str2[i-1])
			return -1; //str1 comes first, alphabetically
		else
			return 1; //str2 comes first
	}
	
	/****
		OK, we aren't done yet!  Consider this: if str1 = "ABC" and str2 = "A", 
		then we'd be out of the while loop but exactlyEqual would still be true!
		
		This case happens when strlen(str2) < strlen(str1), so we can just
		check for that.  In this case, we decide that str2 comes before str1,
		alphabetically.
	****/
	if(strlen(str2) < strlen(str1))
	{
		return 1;
	}
	else //they legitimately are equal!
		return 0;
}

int atoi(char str[])
{
	//it's up to us to deal with bad input, so we are dealing with it by 
	//ignoring it.  We assume that all input strings hold valid integer
	//representations with one exception: we are going to allow the user to put
	//in leading zeros, like "0001000".  We are going to remove those leading 
	//zeros, since it will help us with atod later
	
	/****
		It's actually unintuitive how to do this.  The simplest way is to find
		the length of the string, then work backwards.
	****/
	
	//first, we might get a negative.
	int startIndex = 0;
	int sign = 1;
	if(str[0] == '-')
	{
		sign = -1; //this will be multiplied in at the end
		startIndex = 1; //this lets us skip that character
	}
	
	//now deal with leading zeroes
	while(str[startIndex] == '0') //remember, the zero character, not the number
		startIndex++;
	
	int len = strlen(str);
	int retVal = 0;
	for(int i = startIndex; i < len; i++)
	{
		retVal = retVal*10 + (str[i] - 48);
		/****
			huh? If the numbers 0 through 9 are represented by the numerical
			values 48 through 57, then if we subtract 48 from the character, we
			end up with the integer.  Watch:
			
			if '7' is represented by the number 55, then 55-48 = 7, the integer
			we want
		****/
	}
	return sign*retVal; //remember, it may be negative!
}

//Ahh atod. This function is difficult if you try to do it before you write
//atoi, but it is far simpler if you have atoi first.  Still hard though...
double atod(char str[])
{
	/****
	we are going to do this in stages. First, extract the part before the 
	decimal.  This is an integer, so we will read it using atoi.
	
	Next, extract the part after the decimal, if it exists.  If it does, then
	this will ALSO be treated as an integer. We'll convert it.
	
	Finally, take that last integer and divide it by 10 raised to the power
	of however many digits we have after the decimal that are nonzero.
	****/
	
	//in order to extract, we will use a temporary character array.  Integers 
	//are at most 9 digits, so:
	char tmp[10] = {0}; 
	int startIndex = 0;
	double sign = 1;
	if(str[0] == '-')
	{
		sign = -1;
		startIndex = 1;
	}
	//For this, we don't need to worry about leading zeros, atoi will deal with
	//that
	int intPart = 0;
	int i = startIndex;
	int j = 0;
	while(str[i] != '.' && str[i] != 0 && i < 10)
	{
		tmp[j] = str[i];
		i++;
		j++; //need two, since we might start at 1
	}
	//convert tmp
	intPart = atoi(tmp);
	
	if(str[i] == '.')
	{
		i++; //increment to get away from the decimal
		//hard case: extract the integers. We can re-use tmp
		j = 0;
		while(str[i] != 0 && j < 10)
		{
			tmp[j] = str[i];
			j++;
			i++;
		}
		//now, how many digits is stored in decPart?  We need to search tmp
		//backwards for the first non-zero character
		int numDigits = strlen(tmp);
		j = numDigits-1;
		while(tmp[j] == '0' && j >= 0)
		{
			numDigits--;
			tmp[j] = 0;
			j--;
		}
		//convert it again
		double decPart = (double)atoi(tmp);
		
		
		cout << decPart << endl;
		decPart = decPart/pow(10.0,1.0*numDigits-1);
		cout << decPart << endl;
		//add them together and return
		return sign*((double)intPart + decPart);
	}
	else
	{
		return (double)intPart; //easy case - no decimal point
	}
	
	
}

//findchar is much simpler than atod.
int findChar(char str[], char c)
{
	//initialize the return value to -1, because if we do not find the
	//character, we return a negative value
	int foundIndex = -1;
	
	//We can either get the string's length using strlen, or find it ourselves.
	//I'm going to use strlen for clarity.
	int len = strlen(str);
	
	//we need to indicate somehow that we found the character, so that we don't
	//keep looping, so there are two conditions here: either we run out of 
	//string, or we find the character.  If we find the character, foundIndex
	//will not be -1 anymore
	for(int i = 0; i < len && foundIndex == -1; i++)
	{
		if(str[i] == c)
			foundIndex = i; //this will break us out of the loop
	}
	
	//just return it
	return foundIndex;
}

/*
	findFirstOf is hard if you do not use findChar, but it is much easier if you
	do.  One thing to note: the way the specification is written, the following
	must happen:
	
	Let's assume we are searching the string "Hello" for characters in the 
	string "olleH".  We should see the output value 4, since 'o' was the first
	character in the search string found.  That is, although the search string
	contains the character 'H', which is the first character in the string we 
	are searching, we should still return 4, since 'o' is the first character
	we will be looking for.
	
	The above paragraph simplifies down to this: just search the first string
	for all characters in the search string, starting at the first.  *As soon
	as you find ANY character in the search string, just return.*  It makes 
	life a LOT easier.
	
*/
int findFirstOf(char str1[], char str2[])
{
	//let's get the string length for str 2
	int len = strlen(str2);
	
	//a return index, as above, initialized to -1
	int retIndex = -1;
	
	//we are looping over str2, but also leaving the loop if we find a character
	for(int i = 0; i < len && retIndex == -1; i++)
	{
		//if we find the character, retIndex will be anything but -1, otherwise, 
		//it will stay -1 and we'll keep looping
		retIndex = findChar(str1, str2[i]);
	}
	
	//return t
	return retIndex;
}


int main()
{
	char str1[] = "ABC";
	char str2[] = "ABC";
	cout << strlen(str1) << endl;
	cout << strlen(str2) << endl;
	cout << strcmp(str1,str2) << endl;
	
	//A particularly difficult value for atoi would be a negative number with
	//trailing zeros, like -00010900.  This value is negative, includes the full
	//range of characters, and has two trailing zeros and three leading zeros
	char numVal[] = "-00010900";
	cout << atoi(numVal) << endl;
	char numVal2[] = "-10.0012500";
	cout << atod(numVal2) << endl;
	
	//let's search our existing strings for various characters, to test findChar
	cout << findChar(numVal, 'A') << endl; //I should see -1
	cout << findChar(numVal, '0') << endl; //I should see 1
	cout << findChar(numVal, '-') << endl; // I should see 0;
	cout << findChar(str1,'C') << endl; //I should see 2, good test of strlen
	
	//now we test findFirstOf.  We'll need a new string
	char str3[] = "Helloe";
	char str4[] = "AbDEe";
	cout << findFirstOf(numVal,str3) << endl; //I should see -1
	cout << findFirstOf(str3, str4) << endl; //I should see 1
}

























