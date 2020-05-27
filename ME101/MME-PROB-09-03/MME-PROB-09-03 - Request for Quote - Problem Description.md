Problem Number: MME-PROB-09-03
------------------------------

Problem Title: Request for Quote
================================

Code filename: request_for_quote.cpp

The problem is intended as an exercise in using parallel arrays to store, find, and retrieve data.

Ryan is designing an advanced LEGO EV3 floor sweeper. He is considering a number of possible design options. He would like your assistance in analyzing the differences in cost between these designs.

Ryan has a catalog of the available LEGO parts in a file called catalog.txt. There are at most 30 parts in the catalog. Each line of this file has information for a LEGO part:
* description
* part number
* price per part

Ryan has stored the bill of materials for his various designs in a file called BOMs.txt. For each design, Ryan starts by listing the name of the design. Then, he gives the number of different parts used in the design. Then Ryan lists each of the part numbers and the quantity used in that design. This is repeated in the file for each of the designs. There are an unknown number of designs that Ryan has created.

Your job is to generate a series of price quotes for the BOMs provided. Output is to be sent to a file called BOM_costs.txt.

For each design, output:
* design name
* description of each part, the quantity used in the design, and a subtotal for the cost of that part (do not output any part descriptions that are not used in the design)
* total part cost of the design

Overall, output the name of the design with the lowest cost. Also, output the name of the design with the highest total number of parts used.

### Sample Input

A sample catalog.txt and a sample BOMs.txt file are provided.

### Sample Output

A sample output file (BOM_costs.txt) is provided for the given sample input files.

### Time Target

<table>
  <tr>
    <th> Time to Complete </th>
    <th> Rating </th>
  </tr>
  <tr>
    <th> Less than 45 minutes </th>
    <th> \* \* \* </th>
  </tr>
  <tr>
    <th> 45 to 60 minutes </th>
    <th> \* \* </th>
  </tr>
  <tr>
    <th> More than 60 minutes </th>
    <th> \* </th>
  </tr>
</table>


© 2019 DAVID LAU ALL RIGHTS RESERVED
