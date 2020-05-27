    #include <iostream> //typo here
    #include <cmath> //sqrt lives here!
    using namespace std; //using, not use
    
   		int main() //main didn't have a return type, int
    		{
       		double x, y; //semicolon!
            cin >> x;
//lots of problems below!
        		y = pow(x,2.0) + 5*x + sqrt(x + 2) - (1.0/2)*x;
        		cout << y;
    		}

