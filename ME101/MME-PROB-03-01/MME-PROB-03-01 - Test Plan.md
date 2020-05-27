Test Plan
---------
Problem Number: MME-PROB-10-03
------------------------------

Problem Title: Numerical Notation
================================

Each form is checked with the following types of numbers:
* large positive number with at least 16 digits specified, in fixed notation
* large positive number with at least 16 digits specified, in scientific notation
* large negative number with at least 16 digits specified, in fixed notation
* large negative number with at least 16 digits specified, in scientific notation

### qty_output_lines.py

The output contains 6 non-empty lines.

### default_format.py

The first output has exactly 6 digits of precision. All digits must match the expected value.

### 2_digits.py

The second output has exactly 2 digits of precision. All digits must match the expected value.

### 16_digits.py

The third output has exactly 16 digits of precision. The first 14 characters must match the expected value.

### fixed_6_digits.py

The fourth output has the correct number of digits. The specified digits of the input need to match, up to 14 characters or the length of the output string.

### fixed_0_digits.py

The fifth output has 0 digits after the decimal point.

# Possible variations or erroneous approaches

*

© 2019 DAVID LAU ALL RIGHTS RESERVED
