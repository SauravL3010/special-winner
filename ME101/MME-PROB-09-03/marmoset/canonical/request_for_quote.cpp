/*
request_for_quote.cpp

canonical solution

© 2019 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <iomanip>
#include <fstream>

const int CATALOG_SIZE = 30;

struct catalog
{
    std::string description[CATALOG_SIZE];
    int part_num[CATALOG_SIZE];
    double price_per[CATALOG_SIZE];
    int size;
};

struct summary_data
{
    std::string design_lowest_cost_name;
    double design_lowest_cost = -1;
    bool design_lowest_cost_initialized = false;
    std::string design_most_parts_name;
    int design_most_part_qty = -1;
    bool design_most_parts_initialized = false;
};

void output_summary(std::ofstream & fout, summary_data to_output)
{
    fout << "The design with the lowest cost is "
         << to_output.design_lowest_cost_name
         << "." << std::endl;
    fout << "The design with the most number of parts is "
         << to_output.design_most_parts_name
         << "." << std::endl;
}

void catalog_lookup(catalog the_catalog,
    int part_partnum,
    std::string & part_description,
    double & part_price_per)
{
    part_description = "";

    int catalog_index = 0;
    while (part_description == "" &&
        catalog_index < the_catalog.size)
    {
        if (the_catalog.part_num[catalog_index] == part_partnum)
        {
            part_description = the_catalog.description[catalog_index];
            part_price_per = the_catalog.price_per[catalog_index];
        }
        catalog_index++;
    }
}

void process_parts(std::ifstream & fin_BOMs,
    std::ofstream & fout,
    catalog the_catalog,
    int design_num_parts,
    double & design_cost,
    int & design_part_qty)
{
    std::string part_description;
    int part_partnum = 0;
    double part_price_per = 0.0;
    int part_qty = 0;
    double part_subtotal = 0.0;

    design_cost = 0.0;
    design_part_qty = 0;

    for (int part_num = 0; part_num < design_num_parts; part_num++)
    {
        fin_BOMs >> part_partnum >> part_qty;

        catalog_lookup(the_catalog, part_partnum, part_description, part_price_per);
        part_subtotal = part_qty * part_price_per;
        design_cost += part_subtotal;
        design_part_qty += part_qty;

        fout << std::setw(25) << part_description
         << std::setw(12) << part_qty
         << std::setw(10) << part_subtotal
         << std::endl;
     }
}

summary_data process_BOMs(std::ofstream & fout,
    catalog the_catalog,
    summary_data summary_so_far)
{
    std::ifstream fin_BOMs("BOMs.txt");

    std::string design_name;
    int design_num_parts = 0;
    int design_total_part_qty = 0;
    double design_cost = 0.0;

    while (fin_BOMs >> design_name)
    {
        fout << design_name << std::endl;

        fin_BOMs >> design_num_parts;

        process_parts(fin_BOMs, fout, the_catalog, design_num_parts, design_cost, design_total_part_qty);

        fout << "$" << design_cost << std::endl << std::endl;

        if (design_cost < summary_so_far.design_lowest_cost ||
            summary_so_far.design_lowest_cost_initialized == false)
        {
            summary_so_far.design_lowest_cost_name = design_name;
            summary_so_far.design_lowest_cost = design_cost;
            summary_so_far.design_lowest_cost_initialized = true;
        }

        if (design_total_part_qty > summary_so_far.design_most_part_qty ||
            summary_so_far.design_most_parts_initialized == false)
        {
            summary_so_far.design_most_parts_name = design_name;
            summary_so_far.design_most_part_qty = design_total_part_qty;
            summary_so_far.design_most_parts_initialized = true;
        }
    }

    fin_BOMs.close();
    return summary_so_far;
}

int main(int argv, char * args[])
{
    std::ifstream fin_catalog("catalog.txt");
    std::ifstream fin_BOMs("BOMs.txt");
    std::ofstream fout("BOM_costs.txt");

    if (!fin_catalog)
    {
      std::cout << "Unable to open catalog.txt." << std::endl;
      return -1;
    }

    if (!fin_BOMs)
    {
      std::cout << "Unable to open BOMs.txt." << std::endl;
      return -1;
    }

    catalog the_catalog;
    the_catalog.size = 0;

    while (fin_catalog >> the_catalog.description[the_catalog.size]
            >> the_catalog.part_num[the_catalog.size]
            >> the_catalog.price_per[the_catalog.size])
    {
        the_catalog.size++;
    }

    summary_data summary_all;

    fout << std::fixed << std::setprecision(2);

    summary_all = process_BOMs(fout, the_catalog, summary_all);

    output_summary(fout, summary_all);

    fin_catalog.close();
    fin_BOMs.close();
    fout.close();
    return 0;
}
