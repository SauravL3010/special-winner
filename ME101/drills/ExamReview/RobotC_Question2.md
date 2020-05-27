## Question 2

A robot is placed in the bottom left corner of a square room.  It is in the standard lab configuration, except the color sensor has been rotated 90 degrees so that, if there is an obstacle directly in front of the robot, the robot can sense its color.  In addition, the robot has a Swiffer Sweeper™ cloth attached underneath it.  The swiffer cloth is 15cm wide.

The walls of the room are yellow, and obstacles can be either blue or red.  A red obstacle is small, and the robot can simply push it over by increasing its motor power to 100% for 1s.  During this pushing phase, the robot will not move forward, and it may resume its previous course.  A blue obstacle is too big.  Once found, the robot must wait for help before continuing.  The human supervisor will periodically check on the robot.  If it is waiting for help, the human will remove the blue obstacle and push the orange button.

A function, turn90(int dir), has been provided to you.  It turns the robot
90 degrees.  If dir == 1, it will turn the robot clockwise.  Otherwise, it
will turn it counter-clockwise.

Your task is to write two functions and one main program that will enable the robot to sweep the entire floor.

1. State at least one assumption that you will make to solve this problem.
2. State at least one problem with the above plan that will make it difficult for the robot to complete its task.
3. Write the program according to the rules below:
- Write a function that takes in a desired motor power and drives the robot forward at the given power until it hits an obstacle.  The function must return the color of the obstacle.
- Write a second, nontrivial function of your choosing that will assist in the task.
- Write a task main that calls your two functions above, and includes any other code that you need to ensure that the robot sweeps the entire floor.
