## Robot C Question 1

Captain Star is making a space-age vending machine robot that senses when people are near, then tries to sell them things.  A function, giveCandy(), has already been written for you.  It gives the person their selected candy.  Help Captain Star by writing the following program:

- The vending machine displays a friendly message until someone comes within 100cm of its sonar sensor.  
- When someone is in range, the display changes and prompts them to make a selection.
  - If button 1 is pushed, they are given a small candy
  - If button 2 is pushed, they are given a large candy
  - If button 3 is pushed, they are asked if they want a chocolate or a Curly Wurly, and respond using the buttons.
- Once a selection has been made, you must call the function giveCandy.
- You must keep track of how much money has been made.  Small candies cost \$1, large candies cost \$2, chocolates cost \$3, and Curly Wurlies cost \$4.
- If the touch sensor is pressed at **any** time during the process, the robot must output how much money it has made for 3 seconds, then the program ends.
