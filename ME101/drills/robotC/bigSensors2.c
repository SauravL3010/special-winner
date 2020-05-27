task main()
{
	//initialize sensors
	SensorType[S1] = sensorSONAR;
	SensorType[S2] = sensorTouch;

	//clear timer
	clearTimer(T1); //this is the main timer, for 3 minutes

	//state
	int state = 1;

	//max time
	const int MAX_TIME = 60*3*1000;

	while(state != 5)
	{
		//as in the previous question, we want to use one
	  //set of if statements
		if(state == 1)
		{
			motor[motorA] = 0;
			motor[motorC] = 0;
		}
		if(SensorValue[S1] < 100)
		{
			state = 2; //this won't be super relevant

			//clear the other timer
			clearTimer(T2);

			//set the motors
			motor[motorA] = -100;
			motor[motorC] = -100;

			//we actually need to wait on four things
			//touch, button, T2, and T1
			while(nNxtButtonPressed != 3 && SensorValue[S2] == 0 && time1[T1] < MAX_TIME && time1[T2] < 3000){}

			//return to state 1 if T2 expired, otherwise let the rest of the if statements
			//handle the transition.
			if(time1[T2] > 3000)
				state = 1;
		}
		if(nNxtButtonPressed == 3)
		{
			//we aren't waiting on release or anything, just go
			state = 3;

			//set motors
			motor[motorA] = 100;
			motor[motorC] = 100;

			//need to wait on three things: ultrasonic, timer, and touch
			while(SensorValue[S1] < 100 && SensorValue[S2] == 0 && time1[T1] < MAX_TIME){}

			//we aren't going to transition state here, we'll let the if statements below
			//do that
		}
		if(SensorValue[S2] == 1)
		{
			state = 4;
			//spin!
			motor[motorA] = 100;
			motor[motorC] = 100;

			clearTimer(T2);

			//we need to wait on the buton, T2, and T1
			while(nNxtButtonPressed != 3 && time1[T1] < MAX_TIME && time1[T2] < 3000){}

			//If T2 ran out, return to state 1
			if(time1[T2] > 3000)
			{
				state = 1;
			}

			//Again, the if statements will handle the rest of the state
			//transitions for us
		}
		if(time1[T1] > MAX_TIME)
		{
			state = 5;
		}
	}
	//so now stop
	motor[motorA] = 0;
	motor[motorC] = 0;
}
