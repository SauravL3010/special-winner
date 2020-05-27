/*
missing_semi-colon.cpp

2016-08-25 - original version

© 2017 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
	srand (time(NULL));

	char play = 'x';
	char play_again = 'y';
	char difficulty = '1';

	cout << "Let's play 'Rock-Paper-Scissors!" << endl;

	while (play_again == 'y')
	{
		// 1: user always wins (because it looks at the user's play first)
		// 2: computer picks a random play
		// 3: computer picks what the player played last,
		//    which one study indicates is a better strategy
		// 4: computer always wins (because it looks at the user's play first)
		cout << "Choose your difficulty: " << endl;
		cout << "1: Dumb and Dumber" << endl;
		cout << "2: Randomizer" << endl;
		cout << "3: Artificial Intelligence" << endl;
		cout << "4: I'm Invicible!" << endl;
		do
		{
			cout << "Enter 1-4: ";
			cin >> difficulty;
		}
		while (difficulty < '1' || difficulty > '4');

		cout << endl;

		int play_num = 1;
		char last_play = play;
		char computer_play = 'r';
		int player_score = 0;
		int computer_score = 0;

		while (play_num <= 5)
		{
			cout << endl << "Round #" << play_num << " of 5" << endl;
			do
			{
				cout << "Enter your play (r/p/s)";
				cin >> play;
			}
			while (play != 'r' && play != 'p' && play != 's');

			if (difficulty == '1')
			{
				if (play == 'r')
					computer_play = 's';
				else if (play == 'p')
					computer_play = 'r';
				else
					computer_play = 'p';
			}
			else if (difficulty == '2')
			{
				int generate_random = rand() % 3;
				if (generate_random == 0)
					computer_play = 'r';
				else if (generate_random == 1)
					computer_play = 'p';
				else
					computer_play = 's';
			}
			else if (difficulty == '3')
			{
				computer_play = last_play;
				last_play = play;
			}
			else if (difficulty == '4')
			{
				if (play == 'r')
					computer_play = 'p';
				else if (play == 'p')
					computer_play = 's';
				else
					computer_play = 'r';
			}

			if (play == 'r')
				cout << "Your play:     rock";
			else if (play == 'p')
				cout << "Your play:    paper";
			else
				cout << "Your play: scissors";

			cout << "          Computer play: ";

			if (computer_play == 'r')
				cout << "rock" << endl;
			else if (computer_play == 'p')
				cout << "paper" << endl;
			else
				cout << "scissors" << endl;

			if (play == computer_play)
				cout << "This round is a tie." << endl;
			else if ((play == 'r' && computer_play == 's') ||
					 (play == 'p' && computer_play == 'r') ||
					 (play == 's' && computer_play == 'p'))
			{
				cout << "You win this round." << endl;
				player_score++;
			}
			else
			{
				cout << "The computer wins this round." << endl;
				computer_score++;
			}

			cout << "Your score: " << player_score << "                ";
			cout << "Computer score: " << computer_score << endl;

			play_num++;
		}

		cout << endl;
		if (player_score > computer_score)
			cout << "You win this game!" << endl;
		else if (computer_score > player_score)
			cout << "The computer wins this game!" << endl;
		else
			cout << "The game is a tie!" << endl;

		cout << "Would you like to play again?" << endl;
		do
		{
			cout << "Enter y/n: ";
			cin >> play_again;
		}
		while (play_again != 'y' && play_again != 'n');

		cout << endl << endl << endl;
	}


	return 0;
}
