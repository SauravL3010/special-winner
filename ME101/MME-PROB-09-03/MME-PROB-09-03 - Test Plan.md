Test Plan
---------
Problem Number: MME-PROB-09-03
------------------------------

Problem Title: Request For Quote
================================

### output_file_exists.py

### output_text.py

Check for the phrases "lowest cost" and "most ... parts" in output.

### design_names.py

All the names in the BOMs.txt file are found in the output file. None of the names in the master list of design names are found in the output file, that were not listed in the BOMs.txt file.

### part_descriptions.py

The matching part descriptions for each of the listed part numbers is given in the same order as they appear in BOMs.txt.

### design_costs.py

The total costs for each design are calculated correctly, by looking up the cost of each part in the catalog and multiplying by the quantity of that part.

### summary.py

Lowest cost design and design with the greatest quantity of parts are identified correctly.

# Possible variations or erroneous approches

* 

© 2019 DAVID LAU ALL RIGHTS RESERVED
