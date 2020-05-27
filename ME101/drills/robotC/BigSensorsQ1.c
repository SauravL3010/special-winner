task main()
{
	//always initialize sensors
	SensorType[S1] = sensorTouch;
	SensorType[S2] = sensorColorNxtFULL;

	//initialize encoders
	nMotorEncoder[motorA] = 0;

	//initialize the state variable
	int state = 1;

	//we need a big while loop and a bunch of if statements
	while(state != 5)
	{
		/*
		Note: we use a bunch of if statements, rather than an if-else if-else
		structure, since it's possible to transition
        between states very quickly.  We could, for example, transition into 
		state 2 and then immediately into state 3.*/
		if(state == 1 || state == 2)
		{
			motor[motorA] = 50;
			motor[motorC] = 50;
		}
		if(nMotorEncoder[motorA] * 2 * PI * 1.5/360.0 > 500 && state == 1)
		{
			state = 2;
		}
		//red is 5
		if(SensorValue[S2] == 5 && state == 2)
		{
			//not really relevant to keep track of this, you'll see why below
			state = 3;
			clearTimer(T1);
			motor[motorA] = 0;
			motor[motorC] = 0;
			while(time1[T1] < 1000 && SensorValue[S1] == 0){} 
			//*always* wait on the touch sensor

			//go back to state 2, so I didn't really need to keep track of the 4
			//fact that we were in state 3
			state = 2;
		}
		//blue is color 2
		if(SensorValue[S2] == 2 && state == 2)
		{
			//Not really relevant to keep track of this, you'll see why below
			state = 4;
			clearTimer(T1);
			motor[motorA] = 40;
			motor[motorC] = -40;
			while(time1[T1] < 3000 && SensorValue[S1] == 0){} 
			//*always* wait on the touch sensor

			//go back to state 2, so I didn't really need to keep track of the 
			//fact that we were in state 4
			state = 2;
		}
		if(SensorValue[S1] == 1)
		{
			state = 5;
		}
	}
	//we are now in state 5 (otherwise we would not have exited the while loop),
	// so stop.
	motor[motorA] = 0;
	motor[motorC] = 0;
}
