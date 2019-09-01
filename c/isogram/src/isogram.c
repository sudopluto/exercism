#include "isogram.h"

bool is_isogram(const char phrase[])
{
    if(!phrase)
    {
        return false;
    }

    int hist[26] = {0};
    
    while(*phrase)
    {
        char c = *phrase;
        if (c >= 'A' && c <= 'Z')
        {
            
            c = 'a' + (c - 'A');
        }    
        if (c >= 'a' && c <= 'z')
        {
            if (hist[c - 'a']++ > 0)
            {
                return false;
            }
        }
        ++phrase;
    }
    return true;
}
