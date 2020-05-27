Test Plan
---------
Problem Number: MME-PROB-07-03
------------------------------

Problem Title: Coordinate Tracking
==================================

### console_output.py

Check that some output was sent to the console.

### sample_input.py

First three lines of output match given sample output.

### constant_input.py

Output is correct for standard input file lines that don't change.

### num_lines.py

Number of output lines matches number of input file lines.

### randomize.py

Last lines of input file are randomized. Output is correct.

# Possible erroneous approches

* uses while (fin), causing an extra line read
* uses eof(), causing an extra line read
* don't convert degrees to radians
* don't continuously add to current position
* null program

© 2018 DAVID LAU ALL RIGHTS RESERVED
