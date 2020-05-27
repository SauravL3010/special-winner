Test Plan
---------
Problem Number: MME-PROB-04-03
------------------------------

Problem Title: Above or Below the Line
======================================

### above.py

Five points, all above the line.

### below.py

Five points, all below the line.

### on_exact.py

Five points, all on the line. For all points, the entered x value is exactly the same as the entered y value.

### on_tolerance.py

Five sets of points, all on the line. For all sets, the difference between the x value and y value is varied to smaller values from 1e-1 to 1e-16 to see if at some point the program identifies the point on the line.

### randomize.py

Five random points.

# Possible variations or erroneous approches

* program outputs all keywords, hoping that just that the appearance of that keyword would cause the test case to pass
* program uses <= when it should be <, or >= when it should be >
* output text is in varying case (lower-case or upper-case)

© 2018 DAVID LAU ALL RIGHTS RESERVED
