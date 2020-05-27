#include <iostream>
#include <fstream>
#include <iomanip>

int main()
{
    std::ifstream fin("medal_count.txt");

    if (!fin)
    {
        std::cerr << "Unable to open medal_count.txt" << std::endl;
        return -1;
    }

    std::string country_name;
    std::string country_most;
    int qty_most = 0;

    while (fin >> country_name)
    {
        int qty_bronze = 0, qty_silver = 0, qty_gold = 0;

        fin >> qty_gold >> qty_silver >> qty_bronze;

        std::cout << std::setw(25) << country_name << "  ";

        for (int bronze_count = 1; bronze_count <= qty_bronze; bronze_count++)
            std::cout << "B";
        for (int silver_count = 1; silver_count <= qty_silver; silver_count++)
            std::cout << "S";
        for (int gold_count = 1; gold_count <= qty_gold; gold_count++)
            std::cout << "G";
        std::cout << std::endl;

        if (qty_gold + qty_silver + qty_bronze > qty_most)
        {
            country_most = country_name;
            qty_most = qty_gold + qty_silver + qty_bronze;
        }
    }

    std::cout << std::endl;
    std::cout << "The country with the most medals is " << country_most
        << " with " << qty_most << " medals earned." << std::endl;

    fin.close();
    return 0;
}
