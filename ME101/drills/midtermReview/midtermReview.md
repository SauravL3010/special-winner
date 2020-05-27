# Midterm Review

## Fix the errors

The code samples below contain errors.  For each question, the description of what the code *should* do is provided.  Identify the errors, correct them, and verify that the new code meets the specification.  

### Question 1
Expected: the user will enter an integer.  The program must verify that the integer is positive or zero.  If not, it should prompt the user to re-enter the integer until it is correct.

	int x = 0;
	cout << "Enter a non-negative integer: ";
	cin >> x;
	if(x < 0)
	{
		cout << "Integer must be positive!";
		return 0;
	}

### Question 2
Expected: The user will enter an integer, n.  The program should compute the sum of all positive integers less than or equal to n.  You do not need to verify that the input is positive.

	int n = 0;
	cout << "Enter the number: ";
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		i += n;
	}
	cout << "The sum is: " << i << endl;

### Question 3
Expected: The array, AR, contains numbers from an experiment.  The program must compute the average of these numbers, and display it.

	int AR[5] = {1, 16, 26, 24, 90};
	int avg;
	for(int i = 1; i <= 5; i++)
	{
		avg += AR[i];
		avg = avg/5;
	}
	cout << avg;

### Question 4
Expected: The user will enter an angle in degrees, a speed, in m/s, and a time in seconds.  The program must compute the (x,y) location of a particle travelling at the given speed for the given time.  Assume that the user begins at the origin and angles are measured counterclockwise from the positive x axis.

	int angle = 0, speed = 0, time = 0;
	cout << "What's your angle, speed, and time? ";
	cin >> angle >> speed >> time;
	double x, y;
	x = cos(angle)*speed;
	y = sin(angle)*time;
	cout << "Your (x,y) coordinates are: " << x << "," << y;

### Question 5
Expected: The robot will move forward for 2 seconds, turn clockwise for 2 seconds, move backwards for 2 seconds, and stop.  The robot is in the standard lab configuration.

	motor[motorA] = 50;
	motor[motorB] = 50;
	wait1MSec();
	motor[motorB] = -50;
	wait1MSec(2);
	motor[motorB] = 50;
	motor[motorA] = -50;
	wait1MSec(2);

## Testing
In this section you will be given a piece of code to test, along with a description of what the code should do.  You may assume that all libraries have been included.  You must generate test cases and expected outputs so that the code is sufficiently tested, then you must determine whether or not the code does what is expected.

### Question 1
Expected: The code will determine if a number is a multiple of 13, and output suitably if so.  The number will come from the user.  The number must be positive, non-zero.  The program will continually prompt the user for a new number if the input is not valid.

	int main()
	{
		int n = 0;
		do{
			cout << "Enter a positive, nonzero integer: ";
			cin >> n;
		}while(n >= 0);

		if(n%13 == 0)
		{
			cout << "It is a multiple!";
		}
		else
		{
			cout << "No, it's not a multiple.";
		}
	}

### Question 2
Expected: The user will enter the grade they got in the course, out of 100.  Grades are whole numbers  The code will not verify that this grade is valid.  The program will output the letter grade that they received, according to the following scheme:

- Grade greater than or equal to 80 = A
- Grade between 70 and 79 = B
- Grade between 60 and 69 = C
- Grade between 50 and 59 = D
- Grade between 0 and 49 = F

		int main()
		{
			int grade = 0;
			cout << "Enter your grade: ";
			cin >> grade;
			if(grade > 80)
			{
				cout << "A";
			}
			else if(grade >= 70)
			{
				cout << "B";
			}
			else if(grade >= 60)
			{
				cout << "C";
			}
			else if(grade >= 50)
			{
				cout << "D";
			}
			else
			{
				cout << "F";
			}
		}

## Loops

### Question 1

Without using arrays, write a program that outputs the multiplication table up to 10.  Do not worry about proper output formatting for now.  For example, the first two rows should be output like this:

~~~~
	1 2 3 4 5 6 7 8 9 10
	2 4 6 8 10 12 14 16 18 20
~~~~

### Question 2

Have the user enter a positive integer.  Validate that it is positive.  Determine all factors of that integer (all numbers that divide it evenly), and output them to the console.

## Arrays

### Question 1

In a loop, have the user enter the coefficients of a polynomial whose highest power is at most 5.  Display the polynomial to the screen.

Example:

	User enters: 1 2 3 4 5 0
	Program outputs: x^5 + 2x^4 + 3x^3 + 4x^2 + 5x

	User enters: 0 4 5 93.2 90.2 0.01
	Program outputs: 4x^4 + 5x^3 + 93.2x^2 + 90.2x + 0.01

NOTE: you may have noticed that, although I entered a zero as the last coefficient, I did not print out that zero for the first example.  You may decide to simplify the question by printing out any trailing zeros if you wish. 

### Question 2

As in question 1, have the  user enter the coefficients of a polynomial whose highest power is at most 5.  Your program must output the derivative of the polynomial.

Example:

	User enters: 1 2 3 4 5 0
	Program outputs: 5x^4 + 8x^3 + 9x^2 + 8x + 5

### Question 3

You are interested in getting users to enter responses to a survey.  The survey has three questions, and the answers to each follow a scale from 1 to 10, with 1 being "very dissatisfied" and 10 being "very satisfied".   The questions are:

1. How satisfied are you with your computer?
2. How satisfied are you with your smartphone?
3. How satisfied are you with Dev-C++?

Users will be prompted to enter responses to each question.  Your program must validate their input.  You do not know how many users will use the program, and you may not ask beforehand.

After asking the user all of the above questions, your program should ask if there are any other people who want to do the survey.  If not, the program should output the average rating of all users for all three questions.

**Note:** there are only three questions and, as a result, this question could be solved without using arrays and wouldn't be much of a headache to do so.   The number of questions was kept low because it would be tedious for you to program a fifty question survey.  Nonetheless, **please use arrays to solve this question.**  
