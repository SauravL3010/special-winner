#Arrays: Solutions

##Question 1

        //I can initialize in many ways, but the easiest in this case is:
    	int x[10] = {1,2,3,4,5,6,7,8,9,10};
    	//now, to print, I need a for loop, since I know how big the array
    	//is
    	for(int i = 0; i < 10; i++)
    	{
    		//note: I begin my loop at i = 0, and end when i < 10, NOT
    		//when i <= 10!
    		cout << x[i] << " ";
    	}
	
##Question 2 
	int AR[10] = {0}; //I'm initializing to zero
    for(int i = 0; i < 10; i++)
    {
        cin >> AR[i]; //get the user input, you can prompt if you want
    }
    //print
    for(int i = 0; i < 10; i++)
    {
	    cout << AR[i] << endl; //you may wish to format differently
    }

##Question 3
	//To find the min and the max, I need to first declare variables.
	int min = AR[0];
	int max = AR[0];
	/*
		Since I don't know what values will be inside the array, I have
		to choose SOME initial value to search for.  The most logical
		numbers to choose would be in the array itself, since then I'm
		guaranteed to get it right. 
	*/
	//now I search using a for loop
	for(int i = 0; i < 10; i++)
	{
		if(AR[i] > max)
		{
			max = AR[i]; //just replace the current max with
			//this new biggest value
		}
		//notice: it's an if, not an else if, since max might equal 
		//min
		if(AR[i] < min) 
		{
			min = AR[i]; 
		}
	}
	cout << "Max: " << max << "Min: " << min;
	
##Question 4

	//finding the average means we use a "running average"
	double AR[10] = {0};
	for(int i = 0; i < 10; i++)
	{
		cin >> AR[i]; //might as well have the user enter the values
	}
	
	double avg = 0; //initialization is EXTREMELY important here
	for(int i = 0; i < 10; i++)
	{
		avg += AR[i]; //just keep adding, we do not want to divide
		//yet.
	}
	//now do the division
	avg = avg / 10;
	cout << avg;

##Question 5
 To approach this, note that an array is sorted ascending if, for every element i, element i+1 is equal to or larger than element i.  So, we need to loop through the array, starting at 1 and ending at the second to last element, and compare.

	//create the array and have the user enter the values
	int AR[10] = {0};
	for(int i = 0; i < 10; i++)
	{
	    cin >> AR[i];
	}
	//now we loop through it
	bool isSorted = true; //a boolean will help us to know if we encounter
	//unsorted values
	for(int i = 0; i < 9; i++)
	{
		/*
			We had to loop until i<9 since we are looking one element ahead,
			so when i = 8, i+1 = 9, and we are comparing everything correctly.
		*/
		if(AR[i] > AR[i+1]) //it is not sorted
		{
			isSorted = false;
		}
	}
	if(isSorted == true)
	{
		cout << "Yes, it's sorted!";
	}
	else
	{
		cout << "Nope, not sorted!";
	}

##Question 6
To do this question, we need to search the array every single time we enter a new value.  Unfortunately, there is no efficient method to do this using only arrays.

	int AR[10] = {0};
	int i = 0;
	/*
			We don't know how many times we are going to loop, since the user might
			enter the same number a hundred or more times, so a while loop is 
			appropriate
	*/
	while(i < 10)
	{
		int getFromUser = 0;
		cin >> getFromUser;
		//Now, we need to search the array.
		bool isFound = false;
		for(int j = 0; j < i; j++)
		{
			if(AR[j] == getFromUser)
			{
				isFound = true;
			}
		}
		
		//now, check, and enter if needed
		if(isFound == false)
		{
			AR[i] = getFromUser;
			//increment i only in this case, since we are adding to the array
			i++;
		}
	}

##Question 7
This question is a slight modification from the previous one.  The user will enter values, which may not be unique.  I'll set this up using two arrays: the first array, AR, will store the user's inputs.  The second array, uniqueAR, will store the unique values in AR.  Notice that the two arrays have to be the same size - the user might enter only unique values, so I have no assurances that uniqueAR can be smaller than AR itself.

The program will proceed as follows: once the user enters the data, we will look at each element in AR, compare it to all of the elements in uniqueAR, and add to uniqueAR only if we don't find it.

	int AR[10] = {0};
	for(int i = 0; i<10; i++)
	{
		cin >> AR[i]; //this should be looking familiar by now...
	}
	/*
		So now we need to make uniqueAR.  The problem is: what should we initialize it
		to?  Logically, the first element of AR has to be entered into uniqueAR at some
		point, so uniqueAR should be initialized to the value of the first
		element of AR.  We can't just say uniqueAR should all be zero, since we don't
		know if AR itself will contain 0!
	*/
	int uniqueAR[10];
	for(int i = 0; i < 10; i++)
	{
		//we can't initialize using a variable all at once, we have to do it in a loop
		uniqueAR[i] = AR[1]; 
	}
	
	//this is the index that we will adding new entries at in uniqueAR
	int uniqueIndx = 0; 
	
	for(int i = 0; i < 10; i++)
	{
		//search uniqueAR
		bool isFound = false;
		for(int j = 0; j < uniqueIndx; j++)
		{
			if(uniqueAR[j] == AR[i])
			{
				isFound = true;
			}
		}
		//if we didn't find it, insert the new entry
		if(isFound == false)
		{
			uniqueAR[uniqueIndx] = AR[i];
			uniqueIndx++; //increment, or we will always overwrite
		}
	}
	//let's output uniqueAR to prove it worked
	for(int i = 0; i < uniqueIndx; i++)
	{
		cout << uniqueAR[i] << endl;
	}

##Question 8
The hard part about this problem lies in how we need to organize and manipulate the data in the array.  For instance, the user might enter values so that the array is sorted ascending by default.  This would be nice, but we can't expect it.  So what do we do?  We use the following algorithm:

Every time the user enters a new value, search the array.  We are looking for the point where the entries in the array are *larger* than the value we wish to insert.  Now there's a catch: we need to insert *into* the array.  Let's see an example:

Say the array has the entries 3, 4, 5.  We still have space for 2 more entries.  When the user enters the number  1, the array *should* be set to 1, 3, 4, 5.  We need to move all of the entries currently in the array to the right by one place.  That's the hard part, so let's look at how to code it.

	int AR[5] = {0};
	/*
	Here's our first challenge: we need to initialize the array to SOMETHING, and we
	chose 0.  But what happens if the user enters -100, then 100?  The array would
	hold the values -100, 0, 100!  We will avoid this by keeping track of how
	many numbers are currently in the array.
	*/
	 
	//the number of elements currently in the array is tidily stored in the variable
	//i, below:
	for(int i = 0; i < 5; i++)
	{
	
		//step 1, get the data
		int newVal = 0;
		cin >> newVal;
		//now, we need to figure out where to put it
		int storeIndx = 0;
		bool isFound = false;
		for(int j = 0; j < i; j++)
		{
			if(AR[j] >= newVal && isFound == false)
			{
			/*
			we want to put it here, at j.  We can only set this once, 
			so we use isFound as a flag
			*/
			isFound = true;
			storeIndx = j;
			}
		}
		//OK, we know where to put it.  Now we need to move everything over.
		//We are doing this by traversing the array backwards
		for(int j = 4; j > storeIndx; j--)
		{
			AR[j] = AR[j-1];
		}
		AR[storeIndx] = newVal; //that's it!
	}
	//And now let's see it to make sure it worked
	for(int k = 0; k < 5; k++)
	{
	cout << AR[k] << " ";
	}
