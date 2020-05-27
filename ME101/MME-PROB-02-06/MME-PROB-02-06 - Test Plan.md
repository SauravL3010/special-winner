Test Plan
---------
Problem Number: MME-PROB-02-06
------------------------------

Problem Title: Balance Part 1
=============================

### input_prompt.py

Assert that the program prompts for input. The input prompt must include the keyword "weight".

### specified_input_1.py

Run the program with the input specified in the problem description:
  David's weight: 60
  daughter's weight: 20

Assert that the output has a value of 0.53 within tolerance of 0.01.
FAIL MESSAGE:
Input >
David's weight : 60
daughter's weight: 20
Output >
Outputted value did not match expected value. Expected output to be between 0.52 and 0.54.

PASS MESSAGE:
Input >
David's weight : 60
daughter's weight: 20
Output >
Outputted value within expected range of 0.52 to 0.54.

### specified_input_2.py

Run the program with the input specified in the problem description:
  David's weight: 73
  daughter's weight: 32

Assert that the output has a value of 0.70 within a tolerance of 0.01.

FAIL MESSAGE:
Input >
David's weight : 73
daughter's weight: 32
Output >
Outputted value did not match expected value. Expected output to be between 0.69 and 0.71.

PASS MESSAGE:
Input >
David's weight : 73
daughter's weight: 32
Output >
Outputted value within expected range of 0.69 to 0.71.

### randomized_input.py

Run the program with 10 sets of randomized inputs. David's weight is between 50 and 100. The daughter's weight is between 15 and 40.

Assert that the output is within the expected value with a tolerance of 0.01.

### output_units.py

Assert that the output states that the units are in meters.

# Possible variations or erroneous approches



© 2019 DAVID LAU ALL RIGHTS RESERVED
