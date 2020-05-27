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
Problem Number: MME-PROB-08-01
------------------------------

Problem Title: Time of Flight Function
======================================

### check_filename.py

### run_Makefile.py

Check if the time_of_flight() function has a return statement. This is done by enabling compiler warnings and looking for the following warning messages:

    "warning: control reaches end of non-void function"
    "warning: no return statement in function returning non-void"

Check if the compilation was successful or not.

### run_function.py

Check if the compilation was successful or not.

Run the program with five different initial velocities to check if the calculation was done correctly. Check for very small values as well as very large values.

© 2017 DAVID LAU ALL RIGHTS RESERVED
