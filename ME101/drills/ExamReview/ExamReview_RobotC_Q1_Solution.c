void giveCandy()
{
	displayString(0,"Enjoy!");
}

task main()
{
	//set up my sensors.  I need both SONAR and TOUCH
	SensorType[S1] = sensorSONAR;
	SensorType[S2] = sensorTouch;

	int cash = 0;

	//loop on the touch sensor
	while(SensorValue[S2] == 0)
	{
		//display A friendly message
		displayString(0,"A friendly message");
		/*
			Yes, I know that was a bad joke...either way, I didn't say in
			the question that you needed to actually explain to the user
			how to buy candy...that would have made a lot of sense, but
			for an exam it would have just been a bunch of writing that you
			didn't need to do!

			Hence, a BIG assumption I'm making here is that the user knows
			how to work the vending machine
		*/

		/*
			check to see if someone is in range.  You might be wondering why I'm
			using if statements instead of while loops.  I want to be sure that  
			the touch sensor can end the program at any time.  The outer loop
			is already waiting on the touch seensor, and it just keeps looping.
			So, I will only wait for things I *need* to wait for.  
		*/
		if(SensorValue[S2] < 100)
		{
			if(nNxtButtonPressed == 1)
			{
				//They are buying a small candy.  Note: We are making an
				//assumption that the giveCandy function knows what type of candy
				//we are giving out
				giveCandy();
				cash += 1;
			}
			else if(nNxtButtonPressed == 2)
			{
				giveCandy();
				cash += 2;
			}
			else
			{
				/*
					Here, we need to wait on a second button press.  However,
					the instructions also state that we must wait on the touch
					sensor AT ALL TIMES.  So we need to wait on both.

					Also, notice that I did not say we had to wait on button release.
					I simplified this question somewhat to how it might appear on an exam
				*/
				while(nNxtButtonPressed != 1 && nNxtButtonPressed != 2 && SensorValue[S2] ==0)
				{}

				//give candy if the touch sensor wasn't presed
				if(SensorValue[S2] == 0)
				{
					//they wanted a candy
					giveCandy();
					if(nNxtButtonPressed == 1)
					{
						cash += 3;
					}
					else
					{
						cash += 4;
					}
				}

			}
		}
	}

	//we are done, so output and end
	displayString(0,"Cash: %d",cash);
	wait1Msec(3000);
}
