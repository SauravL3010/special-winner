# Midterm Review: Solutions

Note: the solutions below are just one way that the question can be solved. If
you solved the problems a different way but the code is reasonably efficient and
reasonably stylistically correct, that's fine.  Check with a TA if you're not
sure.

The suggested test cases are **not** comprehensive.  You should think about
more test cases to use as well.

## Fix the errors

### Question 1

The error in this problem is that we should be using a while loop
(or a do-while), to validate user input.  We should not just exit the program if
the user enters something incorrect.  One possible solution is:

~~~~
	int x = 0;
    do{
      cout << "Enter a non-negative integer: ";
    	cin >> x;  
    }
  	while(x < 0);
~~~~
Suggested test cases:
- x = 1 (should pass)
- x = 0 (should pass, boundary case)
- x = -1 (should re-prompt)

### Question 2

The problem here is that we are adding n to i.  i is an index variable of the
for loop, so it is not available outside of that loop.  Furthermore, we don't
want to add n every time, we want to add integers less than or equal to n.

To solve this, we need to introduce a new sum variable, set it to zero, and
add *i* to it every time through the loop, like so:


  	int n = 0;
  	cout << "Enter the number: ";
  	cin >> n;
     int sum = 0;
  	for(int i = 0; i < n; i++)
  	{
  		sum += i;
  	}
	  cout << "The sum is: " << sum << endl;

Suggested test cases:
- n = 1 (should output 1)
- n = 10 (should output 55)

### Question 3

There are four errors.  First, avg is not initialized to zero, so we will get a
random value stored in it.  Second, avg is an int, but we will be dividing, so
we should really use a double.  Third, we should divide once the for loop is
done, otherwise we will divide too many times and compute too small an average.
Finally, the for loop should loop from array index 0 to array index 4, not from
1 to 5.

    int AR[5] = {1, 16, 26, 24, 90};
    double avg = 0.0;
    for(int i = 0; i < 5; i++)
    {
      avg += AR[i];
    }
    avg = avg/5;
    cout << avg;

Suggested test cases:
- Since there is only one array, there are no suggested test cases.  Compute the average by hand and verify.

### Question 4

First, the angle, speed, and time should all be doubles.  Next, the angles are entered in degrees, but sin and cos take radian arguments, so the angle must be converted.  Finally, the actual calculation for x and y are not correct (see below):

    double angle = 0.0, speed = 0.0, time = 0.0;
    cout << "What's your angle, speed, and time? ";
    cin >> angle >> speed >> time;
    double x = 0.0, y = 0.0; //note: we don't NEED to initialize these
      //but we should
    x = cos(angle*M_PI/180.0)*speed*time;
    y = sin(angle*M_PI/180.0)*speed*time;
    cout << "Your (x,y) coordinates are: " << x << "," << y;

Suggested test cases:
- Enter a speed of 0 and arbitrary angle and time, should see (0,0)
- Enter a time of 0 and arbitrary speed and angle, should see (0,0)
- Enter a time of 1, speed of 1, and angle of 45, should see (0.7, 0.7)

### Question 5

Since the robot is in the standard lab configuration, motors A and C are connected,
motor B is not connected.  Second, the wait1Msec function is not used correctly.
Syntax-wise, it should be wait1Msec, not wait1MSec (notice the capital S).  We
also need to provide a delay in *milliseconds*, not seconds.  Finally, in order
to move backwards, both motors need to be set to negative values, not just one.

motor[motorA] = 50;
motor[motorC] = 50;
wait1Msec(2000);
motor[motorC] = -50; //move clockwise
wait1Msec(2000);
motor[motorA] = -50; //this will set both motors to move backwards
wait1Msec(2000);

## Testing

### Question 1

We'll test the do-while loop first.  According to the program specification:

- Entering a negative number will result in a re-prompt for input
- Entering 0 will also result in a re-prompt for input (this is the edge case)
- Entering a positive number will result in passing the loop

Note: the loop condition is backwards, so automatically we will see that this
code doesn't work as expected!  We can't progress any further in the program
until we correct this bug.  The while condition should read:

    while(n <= 0);

Replace the current while loop condition with the one above to continue testing.

Next, we want to test that if statement.  Assuming we made the above fix:

- Entering 13, 26, 39, etc should result in the output "It is a multiple!"
- Entering 12 should result in the output "No, it's not a multiple."

This is what we should see, so the rest of the program meets the specification.

### Question 2

We need to test all edge cases and all cases within the boundaries.  Since
there are so many cases, we will use the notation of: enteredGrade->output.  For instance, 80->A means "if I enter 80, I should see "A""

- 90->A
- 80->A (edge case)
- 75->B
- 70->B (edge case)
- 65->C
- 60->C (edge case)
- 55->D
- 50->D (edge case)
- 45->F (no edge cases for this one)

The program does NOT meet the specification, since the second test case will
produce B, not A.

## Loops

### Question 1

We need a double loop for this one, but not much else.

    #include <iostream>
    using namespace std;

    int main()
    {
    	for(int i = 1; i <= 10; i++)
    	{
    		for(int j = 1; j <= 10; j++)
    		{
    			cout << i * j << " ";
    		}
    		cout << endl; //end line after the second for loop!
    	}
    }

### Question 2

    #include <iostream>
    using namespace std;

    int main()
    {
    	int n = 0;
    	do{
    		cout << "Enter a positive integer: ";
    		cin >> n;
    	}while(n<=0);

    	//there is no super efficient way to do this, we just need to loop!
    	for(int i = 1; i < n; i++)
    	{
    		//I could have gone only until n/2, but that doesn't save a TON
    		//of efficiency and on a midterm would not really be needed
    		if(n % i == 0)
    		{
    			cout << i << " is a factor." << endl;
    		}
    	}
    }

## Arrays

### Question 1

In order to do this, we need to get the coefficients, which should be stored in
an array of doubles.  We will get them in a loop.  Then, we will loop through
the array again to output.  If any of the coefficients are zero, we will NOT
output that term.

Keep in mind: this problem as it is written could absolutely be solved without
arrays.  For instance, you might input a coefficient, then output the term,
then keep doing that until you're done.  However, if you don't store the coefficients
you can't use them for any subsequent computations. If this were just the first
part of a larger program, we'd want to store the coefficients.

This is actually a surprisingly complex question.  There are many cases that we
have to consider in order to get the formatting exactly right.  Test the program
below until you are convinced it is correct.

    #include <iostream>
    #include <cmath>
    using namespace std;

    int main()
    {
    	const double TOL = 1e-11; //tolerance - we shouldn't use == for doubles!
    	double coeffs[6] = {0.0};
    	cout << "Enter all 5 coefficients: ";
    	for(int i = 0; i < 6; i++)
    	{
    		cin >> coeffs[i]; //I can read directly into the array,
    		//and so should you!
    	}

    	//now we loop.  Notice, I'm only looping up to index 4, not 5.  Why?
    	//because I need to output the symbol "+" at the end of each term EXCEPT
    	//the last one. The last term is output after the loop
    	for(int i = 0; i < 5; i++)
    	{
    		//don't output if it's zero
    		if(fabs(coeffs[i]) > TOL)
    		{
    			//we don't want to display the 1
    			if(fabs(coeffs[i] - 1) > TOL)
    			{
    				cout << coeffs[i] << "x^" << 5-i;
    			}
    			else
    			{
    				cout << "x^" << 5-i;
    			}

    			//Now we have an interesting challenge.  We need to make sure
    			//we don't output a "+" at the very end if there is no coefficient
    			//(if that coefficient is zero), so:
    			if(i!=4 || (i == 4 && fabs(coeffs[5]) > TOL))
    			{
    				cout << " + ";
    			}
    		}

    	}
    	//have to check for zero again
    	if(fabs(coeffs[5]) > TOL)
    	{
    		cout << coeffs[5];
    	}
    }

### Question 2

This question is actually almost the same as the previous one.  To simplify matters,
we are going to re-use the code above, with slight modification.

    #include <iostream>
    #include <cmath>
    using namespace std;

    int main()
    {
    	const double TOL = 1e-11; //tolerance - we shouldn't use == for doubles!
    	double coeffs[6] = {0.0};

    	//might as well store both arrays
    	double derivCoeffs[6] = {0.0};
    	cout << "Enter all 5 coefficients: ";
    	for(int i = 0; i < 6; i++)
    	{
    		cin >> coeffs[i]; //I can read directly into the array,
    		//and so should you!

    		//let's  compute the derivative all at once
    		derivCoeffs[i] = coeffs[i] * (5 - i);
    	}

    	//now we loop.  Notice, I'm only looping up to index 3, not 4.  Why?
    	//because I need to output the symbol "+" at the end of each term EXCEPT
    	//the last one. The last term is output after the loop
    	for(int i = 0; i < 4; i++)
    	{
    		//don't output if it's zero
    		if(fabs(derivCoeffs[i]) > TOL)
    		{
    			//we don't want to display the 1
    			if(fabs(derivCoeffs[i] - 1) > TOL)
    			{
    				cout << derivCoeffs[i] << "x^" << 4-i;
    			}
    			else
    			{
    				cout << "x^" << 4-i;
    			}

    			//Now we have an interesting challenge.  We need to make sure
    			//we don't output a "+" at the very end if there is no coefficient
    			//(if that coefficient is zero), so:
    			if(i!=3 || (i == 3 && fabs(derivCoeffs[4]) > TOL))
    			{
    				cout << " + ";
    			}
    		}

    	}
    	//have to check for zero again
    	if(fabs(derivCoeffs[4]) > TOL)
    	{
    		cout << derivCoeffs[4];
    	}
    }

### Question 3

We only need one array for this question, which stores the **sum** of the responses.
Otherwise we are going to compute the average as we otherwise would: initialize
all responses to zero, keep a running sum of the responses, and divide at the end.

    #include <iostream>
    #include <cmath>
    using namespace std;

    int main()
    {
    	int responses[3] = {0};
    	int numResponses = 0;
    	int tempResponse = 0;
    	double avgs[3] = {0.0};
    	char keepGoing = 'Y';

    	while(keepGoing == 'Y')
    	{
    		cout << "On a scale of 1 to 10: " << endl;
    		cout << "How satisfied are you with your computer? ";
    		cin >> tempResponse;
    		responses[0] += tempResponse;
    		cout << "How satisfied are you with your smartphone? ";
    		cin >> tempResponse;
    		responses[1] += tempResponse;
    		cout << "How satisfied are you with Dev-C++? ";
    		cin >> tempResponse;
    		responses[2] += tempResponse;

    		numResponses++;

    		cout << "Are there any more people who want to do the survey? Y/N: ";
    		cin >> keepGoing;
    	}

    	//compute the averages, you could use a for loop if you wish
    	avgs[0] = 1.0*responses[0]/numResponses;
    	avgs[1] = 1.0*responses[1]/numResponses;
    	avgs[2] = 1.0*responses[2]/numResponses;

    	cout << avgs[0] << " " << avgs[1] << " " << avgs[2];
    }
