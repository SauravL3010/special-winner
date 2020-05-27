# File IO Drills

Note: there are some text files in the folder on Learn that contained this document.  Those files are going to be used throughout these drill exercises, so please make sure they are in the same folder as your code.

## Concepts

### Question 1

Review the following statements regarding file IO and comment on their correctness.

1. A file has to be created outside of your program before you can write to it.
2. A file has to be created outside of your program before you can read from it.
3. A file that is already open cannot be opened again until we close it.
4. If a file does not open, that means that it doesn't exist

### Question 2

The following code snippets are bad and will cause errors.  However, they will compile.  Comment on the error that is caused by each one, then try to fix them.

#### Part a

Assume that the file myFile.txt exists and is in the same directory as my program.  The program contains the following:

    ifstream fin(myFile.txt);

#### Part b

Assume that the file myFile.txt exists and is in the same directory as my program.  The program contains the following lines:

    ifstream fin("myFile.txt");
    ofstream fout("myFile.txt");
    fout << "Hi!";

#### Part c

Assume that the file myFile.txt is as follows:

    5 1 2 3 4 3

What is wrong with the following code?

    ifstream fin("myFile.txt");
    int newIntAr[10];
    for(int i = 0; i < 10; i++)
    {
      fin >> newIntAr[i];
    }

## File Input

### Question 1

Open the file "file1.txt" as an input file.  It contains a set of 10 integers.  Assume that you know how many integers are in the file (well...you *do*, so it's a valid assumption, I guess...).  Print them all to the console.

### Question 2

Open the file "file1.txt" as an input file.  This time, assume that you do NOT know how many integers are in the file (so you can't use a for loop or a known number of file reads).  Print all of the integers to the console.  

### Question 3

The file "file2.txt" contains an unknown number of *records*.  A record is defined as two lines in the file. The first line is the number of integers that are present on the next line.  The line after that count is **exactly** that many integers.  For example, the first two records in the file are:

    18
    283 250 109 109 380 548 322 231 558 376 38 225 207 135 296 497 302 288
    9
    31 616 473 273 409 390 350 1 209

Line 1 indicates that there are 18 integers in the subsequent line, and line 2 contains those integers.  Line 3 contains the number of integers in the second record, and line 4 contains the 9 integers of that record.

Read each line of integers and print their sum to the console, one sum per line.

### Question 4

The file "file3.txt" describes the motion of a robot moving along a floor.  The file contains an unknown number of records.  A record in this file is defined as a single line that contains exactly two numbers.  The first number is the angle, in degrees, that the robot has turned in the **counter-clockwise** direction.  The second number is the distance, in meters, that the robot travelled after the turn.  For example, the first line of the file is:

26 5

This means that it turned 26 degrees counter-clockwise, then moved 5 meters.

Assuming that the robot begins at the origin (0,0) and facing in the direction of the positive x axis, determine the following:

1. What is the robot's total distance travelled?
2. What are the robot's final (x,y) coordinates after it is done travelling?
3. With respect to the positive x axis, which direction is the robot facing?

## File Input/Output

In this section, you will be writing programs that use files for both files for both input and output.

### Question 1

Open a new file and name it whatever you'd like.  Have the user enter their name, address, and phone number, and print them to the file, formatted however you'd like.

### Question 2

The file "file4.txt" contains a number of records.  Each record consists of a single line in the following format:

    NAME COST SALE (DISCOUNT)

where:

NAME is a string that contains the item name
COST is a double that contains the cost of the item
SALE is a boolean indicating whether the item is on sale, with 1 indicating that it is
DISCOUNT is optional and is only present if the item is on sale.  It indicates the percent discount, and is an integer.

For example, the first two lines of the file are:

    computer 800.99 0
    mouse 20 1 25

The first item, the computer, costs $800.99, and is not on sale.  The second item, the mouse, costs $20 and is on sale for a 25% discount.

Read the file line by line.  Output the pre-tax total, the post-tax total, and the total amount of money I saved through purchasing sale items.  This output must go to a file "purchases.txt".  The file must be formatted nicely using iomanip.

### Question 3

file4.txt contains exactly 7 lines, so you may have chosen to read exactly 7 times.  Re-write file4.txt so that it contains a different number of lines.  Test your program with this new input file.  Your program should not need any modifications to run this new input file.  If it does, make the modifications so that it can run *any* file that you give it that follows the format.
