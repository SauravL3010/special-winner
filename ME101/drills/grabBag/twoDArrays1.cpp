#include <iostream>
using namespace std;

int main()
{
	const int N_PLAYERS = 2;
    const int N_ROUNDS = 2;

    int score[N_ROUNDS][N_PLAYERS] = {0};

    //now get the users to enter their score every round
    for(int i = 0; i < N_ROUNDS; i++)
    {
      cout << "Enter your scores for round: " << i << endl;
      for(int j = 0; j < N_PLAYERS; j++)
      {
        cout << "Player " << j << ": ";
        cin >> score[i][j];
      }
    }

    //Now we need to see who won, and again we need to loop.
    int maxScore = 0;
    int winner = 0; //the array index of the player who won

    //Notice that the for loop is different than the one above.  We are
    //looping over players this time, not rounds.
    for(int i = 0; i < N_PLAYERS; i++)
    {
      int playerScore = 0;
      for(int j = 0; j < N_ROUNDS; j++)
      {
        playerScore += score[j][i];
      }
      //find the max.  Note: we are assuming there are no ties!
      if(playerScore >= maxScore)
      {
        maxScore = playerScore;
        winner = i; //player i so far has the highest score.
      }
    }

    cout << "Player " << winner << " Has won!";
}
