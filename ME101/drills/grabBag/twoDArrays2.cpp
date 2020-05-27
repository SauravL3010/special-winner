#include <iostream>
using namespace std;

int main()
{
	  const int N_STUDENTS = 2;
  		const int N_QUIZZES = 3;

  int grade[N_QUIZZES][N_STUDENTS] = {0};

  //now get the users to enter their score every round
  for(int i = 0; i < N_QUIZZES; i++)
  {
    cout << "Enter your grades for quiz: " << i + 1 << endl;
    for(int j = 0; j < N_STUDENTS; j++)
    {
      cout << "Student " << j + 1 << ": ";
      cin >> grade[i][j];
    }
  }

  //now we need to compute averages and output them
  for(int i = 0; i < N_STUDENTS; i++)
  {
    int avg = 0;
    int minGrade = grade[0][i];
    for(int j = 0; j < N_QUIZZES; j++)
    {
      avg += grade[j][i];

      //check for the minimum, but don't do anything yet
      if(minGrade > grade[j][i])
      {
        minGrade = grade[j][i];
      }
    }

    //remove the lowest score now
    avg -= minGrade;

    //output the average
    cout << "Student " << i << " avg: " << avg/(N_QUIZZES - 1.0) << endl;
  }
}
