# MME Marmoset Standards

## Prompts

* The problem description will specify key words that the program is to use in the prompt.
*

## Types of Tests

### Ability to read inputs

* use pexpect
* search for specified keyword(s)
  * not case-sensitive
  * allow for any whitespace combinations around the keyword, including tabs and end-lines
  * if the specified keyword(s) is not found, terminate the student program and the test
* program self-terminates after submission of valid inputs

### Output generated of the expected form

* search for all numbers in output
  * count number of numbers identified

### Outputted values match expected values
