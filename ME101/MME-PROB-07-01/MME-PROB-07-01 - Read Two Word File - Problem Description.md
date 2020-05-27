Problem Number: MME-PROB-07-01
------------------------------

Problem Title: Read Two Word File
=================================

Code filename: read_two_words.cpp

Write a program that opens and reads a file containing two words, separated by whitespace. The whitespace could be one or more spaces, tabs, or newlines. Output the two words to the screen (console), separated by a space.

The name of the input file is two_words.txt.

It is recommended you use the &lt;fstream&gt; library. In order to open the file, you can declare an ifstream variable. For example, this code will open the file and read a single word from the file:

    ifstream file_in("two_words.txt");
    string in_word;
    file_in >> in_word;
    file_in.close();

### Sample Input

    two_words.txt:
    Hello World!

### Sample Output

    console:
    Hello World!

© 2018 DAVID LAU ALL RIGHTS RESERVED
