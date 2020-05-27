Problem Number: MME-PROB-07-05
------------------------------

Problem Title: Medal Count
==========================

Code filename: medal_count.cpp

Shirley is following the Commonwealth Games and would like to see a more graphical summary of the medal counts. She has been keeping track of the medal statistics in a text file called "medal_count.txt".

Write a program that will read the text file and generate a bar graph showing the medals won by each country, on the console. For each medal won, output the appropriate character 'B', 'S', or 'G'. Output the bronze medals first, then the silver, and finally the gold. Display each country in the order that they appear in the input file.

Also output the name of the country with the highest number of medals along with the total number of medals earned.

Note that the Marmoset test server will use other versions of the input file other than the sample one provided.

### Sample Input

Each line of the text file lists a country along with the number of gold, silver, and bronze medals won. The first three lines of the file are:

    Dominica 0 1 1
    Northern_Ireland 1 7 4
    Malaysia 7 5 12
    ...

There are an unknown number of countries in the file and the countries appear in no particular order.

### Sample Output

            Dominica  BS
    Northern_Ireland  BBBBSSSSSSSG
            Malaysia  BBBBBBBBBBBBSSSSSGGGGGGG
                 ...

### Time Target

<table>
  <tr>
    <th> Time to Complete </th>
    <th> Rating </th>
  </tr>
  <tr>
    <th> Less than 20 minutes </th>
    <th> \* \* \* </th>
  </tr>
  <tr>
    <th> 20 to 30 minutes </th>
    <th> \* \* </th>
  </tr>
  <tr>
    <th> More than 30 minutes </th>
    <th> \* </th>
  </tr>
</table>


© 2019 DAVID LAU ALL RIGHTS RESERVED
