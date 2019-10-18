#include "hamming.h"

#include <stdexcept>
#include <iostream>

namespace hamming {

int compute(const char* a, const char* b) noexcept(false) {
    int ret = 0;

    while (*a != '\0' && *b != '\0') {

        if (*a != *b) {
            ++ret;
        }

        ++a;
        ++b;
    }

    if (*a != *b) {
        throw std::domain_error("");
    }

    return ret;
}

}  // namespace hamming
