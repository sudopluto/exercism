#include "resistor_color.h"

uint16_t colorCode(resistor_band_t c)
{
    return colors_arr[c];
}

const resistor_band_t* colors()
{
    return colors_arr;
}
