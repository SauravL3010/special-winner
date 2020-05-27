Test Plan
---------
Problem Number: MME-PROB-07-02
------------------------------

Problem Title: Coordinates File Read
====================================

### console_output.py

Check that some output was sent to the console.

### target_names.py

Outputted target names match the input file.

### distances.py

Calculated distance values within 0.1% of canonical solution.

### headings.py

Calculated heading values within 1% of canonical solution.

### randomize.py

Provide a random input to verify that the submission has not hard-coded the output.

# Possible erroneous approches

* uses while (fin), causing an extra line read
* uses eof(), causing an extra line read

© 2018 DAVID LAU ALL RIGHTS RESERVED
