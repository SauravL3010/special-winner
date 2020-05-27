/*
transpose_matrix.cpp

2018-04-04 - created

© 2018 DAVID LAU ALL RIGHTS RESERVED
*/

#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

const int MAX_ROW = 20;
const int MAX_COL = 50;

bool read_file(int matrix_store[MAX_ROW][MAX_COL],
    int & num_rows, int & num_cols,
    string filename)
{
    ifstream fin(filename.c_str());
    if (fin)
    {
        fin >> num_rows >> num_cols;
        for (int row = 0; row < num_rows; row++)
        {
            for (int col = 0; col < num_cols; col++)
            {
                fin >> matrix_store[row][col];
            }
        }
        return true;
    }
    else
        return false;
}

void output_transpose(int matrix_store[MAX_ROW][MAX_COL],
    int & num_rows, int & num_cols)
{
    for (int row = 0; row < num_cols; row++)
    {
        for (int col = 0; col < num_rows; col++)
        {
            cout << setw(5) << matrix_store[col][row];
        }
        cout << endl;
    }
}

int main()
{
    int matrix_1[MAX_ROW][MAX_COL] = {0};
    int num_rows = 0, num_cols = 0;

    if (read_file(matrix_1, num_rows, num_cols, "matrix_data.txt"))
        output_transpose(matrix_1, num_rows, num_cols);

    return 0;
}
