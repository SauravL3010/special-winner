//Builds a set of directions and distances for file3
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <cmath>

using namespace std;


int main()
{
	string answer = ""; //I only need one, since it will be overwritten
    ofstream fout("nameFile.txt");
    cout << "What's your first name ";
    cin >> answer;
    fout << answer << endl;
    cout << "What's your last name? ";
    cin >> answer;
    fout << answer << endl;
    cout << "What is your street name? ";
    cin >> answer;
    fout << answer << endl;
    cout << "What is your phone number? Enter without spaces, like this: ";
    cout << "555-555-5555: ";
    cin >> answer;
    fout << answer << endl;
}
















