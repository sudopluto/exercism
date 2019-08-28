#include "darts.h"

#include <math.h>

float cordinate_to_radius(coordinate_t cord);

float cordinate_to_radius(coordinate_t cord)
{
    return sqrt(pow(cord.x, 2) + pow(cord.y, 2));
}

uint8_t score(coordinate_t cord)
{
    float rad = cordinate_to_radius(cord);
    if (rad > 10)
    {
        return 0;
    }
    else if (rad > 5)
    {
        return 1;
    }
    else if (rad > 1)
    {
        return 5;
    }
    else if (rad >=0)
    {
        return 10;
    }
    else
    {
        return 0;
    }
}
