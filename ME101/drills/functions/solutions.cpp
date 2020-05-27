   #include <iostream>
   #include <cmath>
   using namespace std;
    //returns the maximum of three integers, a, b, and c
    int maxOfThree(int a, int b, int c)
    {
      int max = a;
      if(b > max)
        max = b;
      if(c > max)
        max = c;

      return max;
    }

    //given two integers that represent the two non-hypoteneuse sides of a
    //right triangle, computes the square of the hypoteneuse
    //NOTE: Yes, I know there is a function, "hypot", in cmath, that does
    //something similar, but I want an integer and no rounding
    int findHypotSquare(int a, int b)
    {
      return a*a + b*b;
    }

    //given an integer, determines if it is a perfect square
    bool isPerfSquare(int x)
    {
      for(int i = 2; i < x/2 + 1; i++)
      {
        if(i * i == x)
          return true;
      }
      return false;
    }
    
int main()
{
	//part 1
	int x = 0;
	do
	{
		cout << "Enter a perfect square: ";
		cin >> x;
	}while(!isPerfSquare(x));
	cout << x << "Is a perfect square!";
	
	//part 2
	int a = 0, b = 0;
	
	//strictly speaking, this should be two *positive* integers
	cout << "Enter two integers: ";
	cin >> a >> b;
	
	//so my goal is this: to first compute the hypothesis' square, 
	//then to determine if it is, in fact, a perfect square.  
	//I don't need to use hypot or cmath to solve this problem.
	int c = findHypotSquare(a,b);
	if(isPerfSquare(c))
		cout << "Yes, the hypoteneuse is an integer.";
	else
		cout << "No, not an integer.";
		
	double h = hypot(a,b);
	//now, we need to extract the integer part of h, by a cast.
	int intPart = floor(h); //eew...this really shouldn't be done...
	//NOW, we need to remove the integer part from h, and determine if the 
	//remaining number is close to zero, using tolerance
	double decPart = h - intPart;
	if(fabs(decPart) < 1e-6) //arbitrary tolerance
		cout << "Yes, the hypoteneuse is an integer";
	else
		cout << "No, not an integer.";
	
	
	//part 3
	int s1 = 0, s2 = 0, hyp = 0;
	cout << "Enter s1, s2, and hypoteneuse, in that order: ";
	cin >> s1 >> s2 >> hyp;
	
	//first, compute what the square of the hypoteneuse *should* be
	int actualHyp = findHypotSquare(s1,s2);
	
	//next, compare it to the square of the entered hypoteneuse
	if(actualHyp == hyp*hyp)
		cout << "Yes! We have a right angled triangle!";
	else
		cout << "No, we do NOT have a right angled triangle.";
	
	
}
