//function 1
int goToObstacle(int mPower)
{
	motor[motorA] = mPower;
	motor[motorC] = mPower;
	while(SensorValue[S1] == 0)
	{}

	//we've hit an obstacle
	return SensorValue[S2];
}

/*
	I'm planning on methodically sweeping back and forth along the wall.
	So, a way to turn, move, and turn again is needed.  I'll make that
	my second function.

	The input variable is dir, which will be +1 or -1 for clockwise
	or counter clockwise turns.

	I'm going to return a bool.  When I am at the end of the room,
	I will turn *and then hit a wall* before I can turn again. This will
	be returned as "false", indicating we cannot continue and we are
	done.
*/
bool makeTurn(int dir)
{
	//first step, turn 90 degrees.
	turn90(dir);

	//then, drive forward by 15cm
	nMotorEncoder[motorA] = 0;
	motor[motorA] = 40;
	motor[motorC] = 40;
	while(nMotorEncoder[motorA] * 2 * 1.5 * PI / 360.0 < 15 && SensorValue[S1] == 0){}
	if(SensorValue[S1] == 0)
	{
		turn90(dir);
	}
	//Now, stop.  I'll let task main choose what to do next.
	motor[motorA] = 0;
	motor[motorC] = 0;
	return (SensorValue[S1] == 0); //this will return false if the touch
	//sensor was hit
}

task main()
{
	//init sensors
	SensorType[S1] = sensorTouch;
	SensorType[S2] = sensorColorNxtFULL;
	int keepGoing = true;
	int turnDir = 1; //the direction we are turning
	while(keepGoing == true)
	{
		int col = goToObstacle(40);
		if(col == 4 ) //we're at a wall, 4 = YELLOW
		{
			keepGoing = makeTurn(turnDir);
			turnDir = -turnDir; //alternate turning directions
		}
		else if(col == 5) // RED, a small obstacle
		{
			motor[motorA] = 100;
			motor[motorC] = 100;
			wait1Msec(1000);
		}
		else if(col == 2) //blue, a BIG obstacle
		{
			//we wait on the orange button to be pressed
			while(nNxtButtonPressed != 3){}
			while(nNxtButtonPressed == 3){}
		}

	}
}
