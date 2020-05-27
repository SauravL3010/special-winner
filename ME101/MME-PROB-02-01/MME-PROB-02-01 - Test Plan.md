<style>
  p {font-size: 10pt}
  p.Code {font-family: "Courier New";
          font-size: 8pt;
          padding-left: 2em}
  li {font-size: 10pt}
  table {font-size: 8pt}
</style>

Test Plan
---------
Problem Number: MME-PROB-02-01
------------------------------

Problem Title: Read and Print
=============================

### prompt.py

Check if program prompts the user. Check for keyword "enter", not case-sensitive. Also check if the program outputs a prompt before outputting the number entered. Checks for the colon before the number.

### single_digit_int.py

Enter a random single digit integer. Check that the same integer is outputted.

### three_digit_int.py

Enter a random integer between 100 and 999. Check that the same integer is outputted.

### negative_int.py

Enter a random integer between -100 and -999. Check that the same integer is outputted.

### float.py

Check that the program does not read and store a floating-point number. When an integer in inputted, it is expected that the program will only read and store the integer portion of the number.

© 2018 DAVID LAU ALL RIGHTS RESERVED
