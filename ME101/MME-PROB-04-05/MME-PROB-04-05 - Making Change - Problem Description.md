Problem Number: MME-PROB-04-05
------------------------------

Problem Title: Making Change
===================================

Code filename: making_change.cpp

Fiona needs assistance calculating which coins to use when making change.

Write a program that inputs the total amount in dollars and cents, and then outputs the minimum number of coins that would be used to make that amount. The total amount is guaranteed to be less than $10.

Your program does not need to output which coins would be used, only the total number of coins needed.

Canadian coins are:

* toonie ($2)
* loonie ($1)
* quarter (25 cents)
* dime (10 cents)
* nickel (5 cents)

Remember that with no penny, you will need to round the amount to the nearest 5 cents. You may want to use an if statement for your program to accomplish the rounding. You should perform the rounding *before* calculating the number of required coins.

### Integer Division

Remember that in C++, if you divide two values of data type int, that the result will be truncated to an int value.

```
29 / 6 evaluates to 4
117 / 10 evaluates to 11
```

### Modulus Operator (%)

Remember that the modulus operator gives you the remainder of a division operation. For example,

```
29 % 6 evaluates to 5
117 % 10 evaluates to 7
```

### Sample Output 1

    Enter the number of dollars:
    5
    Enter the amount of cents:
    18
    
    Minimum number of coins needed:
    5

Note that this solution corresponds to 2 toonies, 1 loonie, and 2 dimes.

### Sample Output 2

    Enter the number of dollars:
    6
    Enter the amount of cents:
    92
    
    Minimum number of coins needed:
    8

Note that this solution corresponds to 3 toonies, 3 quarters, 1 dime, and 1 nickel.

### Time Target

<table>
  <tr>
    <th> Time to Complete </th>
    <th> Rating </th>
  </tr>
  <tr>
    <th> Less than 10 minutes </th>
    <th> \* \* \* </th>
  </tr>
  <tr>
    <th> 10 to 15 minutes </th>
    <th> \* \* </th>
  </tr>
  <tr>
    <th> More than 15 minutes </th>
    <th> \* </th>
  </tr>
</table>


© 2020 DAVID LAU ALL RIGHTS RESERVED
