/*
secret_message.cpp

2018-04-06 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>

using namespace std;

const int MAX_LENGTH = 99;

int main()
{
    ifstream fin("secret_message.txt");

    string message[MAX_LENGTH];

    string message_word;
    int message_index;
    while (fin >> message_word >> message_index)
    {
        message[message_index] = message_word;
    }

    for (int index = 0; index < MAX_LENGTH; index++)
    {
        cout << message[index] << " ";
    }
    cout << endl;

    fin.close();
    return 0;
}
