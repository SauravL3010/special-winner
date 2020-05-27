/*
filling_potholes.cpp

canonical solution

© 2019 DAVID LAU ALL RIGHTS RESERVED
*/

#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

const int QTY_AVE = 75;
const int QTY_STREET = 75;

double pothole_volume(double radius);
void read_file(std::ifstream & fin, int potholes[QTY_STREET][QTY_AVE]);
double repair_volume(int potholes[QTY_STREET][QTY_AVE],
    int road_number,
    bool is_street);

#ifndef MARMOSET_TESTING

int main()
{
    const double TARGET_VOLUME = 0.25;
    double best_delta_volume = TARGET_VOLUME;
    int best_road_number = 0;
    bool best_is_street = true;
    
    std::ifstream fin("potholes.txt");
    
    if (!fin)
    {
        std::cerr << "Unable to open potholes.txt." << std::endl;
        return -1;
    }
    
    int pothole_map[QTY_STREET][QTY_AVE] = {0};
    
    read_file(fin, pothole_map);
    
    double total_repairs = 0.0;
    for (int street_num = 1; street_num <= QTY_STREET; street_num++)
    {
        total_repairs = repair_volume(pothole_map, street_num, true);
        if (TARGET_VOLUME - total_repairs > 0 &&
            TARGET_VOLUME - total_repairs < best_delta_volume)
        {
            best_delta_volume = TARGET_VOLUME - total_repairs;
            best_road_number = street_num;
        }
    }
    
    for (int avenue_num = 1; avenue_num <= QTY_AVE; avenue_num++)
    {
        total_repairs = repair_volume(pothole_map, avenue_num, false);
        if (TARGET_VOLUME - total_repairs > 0 &&
            TARGET_VOLUME - total_repairs < best_delta_volume)
        {
            best_delta_volume = TARGET_VOLUME - total_repairs;
            best_road_number = avenue_num;
            best_is_street = false;
        }
    }
    
    std::cout << "The next road to repair is " << best_road_number;
    
    if (best_is_street)
        std::cout << " Street." << std::endl;
    else
        std::cout << " Avenue." << std::endl;
    
    return 0;
}

#endif

double pothole_volume(double radius)
{
    return 2.0/3 * M_PI * pow(radius/1000.0, 3);
}

void read_file(std::ifstream & fin, int potholes[QTY_STREET][QTY_AVE])
{
    int street_num = 0;
    int ave_num = 0;
    int pothole_radius = 0;
    
    while (fin >> street_num >> ave_num >> pothole_radius)
    {
        potholes[street_num - 1][ave_num - 1] = pothole_radius;
    }
}

double repair_volume(int potholes[QTY_STREET][QTY_AVE],
    int road_number,
    bool is_street)
{
    double total_volume = 0.0;
    
    if (is_street)
    {
        for (int ave_num = 1; ave_num <= QTY_AVE; ave_num++)
        {
            total_volume += pothole_volume(potholes[road_number - 1][ave_num - 1]);
        }
    }
    else
    {
        for (int street_num = 1; street_num <= QTY_STREET; street_num++)
        {
            total_volume += pothole_volume(potholes[street_num - 1][road_number - 1]);
        }
    }
    
    return total_volume;
}
