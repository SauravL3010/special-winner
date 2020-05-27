Problem Number: MME-PROB-10-04
------------------------------

Problem Title: Coffee Rating
============================

Code filename: coffee_rating.cpp

This problem appeared as Question #4 on the GENE 121 Spring 2014 final exam.

Chris has been experimenting with brewing coffee at home. He is interested in the effect of two parameters on the taste of the coffee: the temperature of the water and coarseness of the grind. He has varied the temperature from 91 to 99 degrees Celsius and has ground the beans on a 4-point scale: 1 is very fine and 4 is very coarse. After tasting each cup of coffee Chris rates it on a scale of 1 to 10: 1 indicating he hated it and 10 indicating he loved it. He has run these experiments a total of three times for all combinations of temperature and coarseness, and has stored all of this experimental data in three files: **coffee1.txt**, **coffee2.txt**, and **coffee3.txt**.

Your program should output which combination of temperature and coarseness resulted in the best cup of coffee. The best cup of coffee is defined as the cup that has the highest average rating across all three experiments. If there is a tie, the cup with the lower temperature is the winner. If there is still a tie, the cup with the lower coarseness is the winner.

### 2D Array Design

It is recommended that you sketch out an 2D array design for tabulating the coffee ratings. What does each row of the array correspond to? What does each column of the array correspond to? What does the value stored in each array element correspond to?

### Function - read_file

Write a function called read_file() that reads the input file and updates the 2D array for tabulating coffee ratings. The function must receive the given information in the following order:

1. already opened input file

2. coffee rating array

### Function - best_coffee

Write a function called best_coffee() that receives the coffee rating array and returns the temperature and coarseness that gave the overall best cup of coffee. The function must receive the coffee rating array as its first parameter. You may add parameters that as necessary.

### Function - main

The main function should do the following:

* Opens the three input files and verifies that they opened correctly.
* Declares an appropriately sized and named 2D array to store the coffee rating data.
* Calls the read_file() function on each of the input files.
* Determines the temperature and coarseness for the best coffee.
* Outputs a suitable message to the console.

### Marmoset Testing Requirements

In order for your code to be evaluated by Marmoset, the main() function must be surrounded by the preprocessor directive MARMOSET_TESTING. Your other functions must not be contained within this preprocessor directive. Here is sample code:

    // function declarations go here

    #ifndef MARMOSET_TESTING

    int main()
    {
        ...

        return 0;
    }

    #endif

    // function definitions go here

### Input Files

A sample is provided for each of the three input files.

Here is an example of what the first three lines of a data file looks like:

    92  4   7
    94  2   3
    96  3   9
    ...

The first row of this file represents a cup of coffee brewed at 92 degrees with a coarseness of 4 and Chris rated it 7 out of 10.

### Sample Output

The sample input files should produce the following output:

The best coffee is made at a temperature of 95 C and with a grind coarseness of 2.

### Time Target

<table>
  <tr>
    <th> Time to Complete </th>
    <th> Rating </th>
  </tr>
  <tr>
    <th> Less than 30 minutes </th>
    <th> \* \* \* </th>
  </tr>
  <tr>
    <th> 30 to 45 minutes </th>
    <th> \* \* </th>
  </tr>
  <tr>
    <th> More than 45 minutes </th>
    <th> \* </th>
  </tr>
</table>


© 2019 DAVID LAU ALL RIGHTS RESERVED
