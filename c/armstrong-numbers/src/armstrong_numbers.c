#include "armstrong_numbers.h"

#include <math.h>
#include <stdio.h>

int numPlaces(int num);

int numPlaces(int num)
{
    int len = 1;
    while(num > pow(10, len))
    {
        ++len;
    }
    
    if (num == pow(10, len))
    {
        ++len;
    }

    return len;

}

int isArmstrongNumber(int num)
{
    int temp = num;
    int sum = 0;
    int len = numPlaces(num);

    while(temp > 0)
    {
        sum += pow(temp % 10, len);
        temp /= 10; 
    }

    return sum == num;
}

