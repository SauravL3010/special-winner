Problem Number: MME-PROB-07-02
------------------------------

Problem Title: Coordinates File Read
====================================

Code filename: coordinates_file_read.cpp

Mike is working on a drone launcher and needs your assistance converting target coordinates from rectangular form to polar form.

The file "targets.txt" contains a list of targets along with rectangular coordinates relative to Mike's current position. The units of measurement are in kilometers.

Write a program that reads the file and for each line in the file outputs:
* name of target
* distance to target (in kilometers)
* target heading (in degrees)

A target heading of zero degrees corresponds to the unit vector (1, 0). Output is to be sent to the console (screen).

It is recommended you use the &lt;fstream&gt; library. In order to read each line in the file, it is suggested to use a while loop of the following form:

    ifstream file_in("targets.txt");
    string in_word;
    double coordinate_x = 0.0, coordinate_y = 0.0;
    while (file_in >> in_word >> coordinate_x >> coordinate_y)
    {
        // process input here
    }
    file_in.close();

### Sample Input

The first three lines of target.txt are:

     London -57.82 -53.21
     St_Jacobs 0 7.91
     Toronto 90.04 22.61

### Sample Output

The following output corresponds to the three lines of input given above:

    London 78.58 222.6
    St_Jacobs 7.91 90
    Toronto 92.84 14.1

### Time Target

<table>
  <tr>
    <th> Time to Complete </th>
    <th> Rating </th>
  </tr>
  <tr>
    <th> Less than 7 minutes </th>
    <th> \* \* \* </th>
  </tr>
  <tr>
    <th> 7 to 10 minutes </th>
    <th> \* \* </th>
  </tr>
  <tr>
    <th> More than 10 minutes </th>
    <th> \* </th>
  </tr>
</table>


© 2018 DAVID LAU ALL RIGHTS RESERVED
