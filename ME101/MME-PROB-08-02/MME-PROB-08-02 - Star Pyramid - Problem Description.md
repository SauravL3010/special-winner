<style>
  p {font-size: 10pt}
  p.Code {font-family: "Courier New";
          font-size: 8pt;
          padding-left: 2em}
  li {font-size: 10pt}
  table {font-size: 8pt}
</style>

PROBLEM DESCRIPTION
-------------------
Problem Number: MME-PROB-08-02
------------------------------

Problem Title: Star Pyramid
===========================

Code filename: star_pyramid.cpp

Complete the program below. The user enters the height of a pyramid of stars and the program should display the pyramid to the console.

Use the following code to start. All that is needed is the implementation of the output_spaces() and output_stars() function. No other code should be modified.

    #include <iostream>

    using namespace std;

    void output_spaces(int quantity_spaces)
    {
      /* write function code here */
    }

    void output_stars(int quantity_stars)
    {
      /* write function code here */
    }

    int main()
    {
      int pyramid_size = 0;

      cout << "Enter the height of the pyramid: ";
      cin >> pyramid_size;

      for (int pyramid_level = pyramid_size;
           pyramid_level > 0;
           pyramid_level--)
      {
        output_spaces(pyramid_level - 1);
        output_stars(2*pyramid_size - 2*pyramid_level + 1);
        cout << endl;
      }

      return 0;
    }

Sample output:

    Enter the height of the pyramid: 7
          *
         ***
        *****
       *******
      *********
     ***********
    *************

© 2017 DAVID LAU ALL RIGHTS RESERVED
