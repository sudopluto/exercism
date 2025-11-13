#include "raindrops.h"

namespace raindrops {

std::string convert(int num) {
    std::string ret{};

    if (num % 3 == 0)
        ret += "Pling";

    if (num % 5 == 0)
        ret += "Plang";

    if (num % 7 == 0)
        ret += "Plong";

    return ret.empty() ? std::to_string(num) : ret;
}

}  // namespace raindrops
