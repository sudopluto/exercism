const double NEG_BAL_RATE{3.213};
const double POS_BAL_RATE1{0.5};
const double POS_BAL_RATE2{1.621};
const double POS_BAL_RATE3{2.475};

const double RATE1_MAX{1000};
const double RATE2_MAX{5000};

// interest_rate returns the interest rate for the provided balance.
double interest_rate(double balance) {
    double rate{0};

    if (balance < 0) {
        rate = NEG_BAL_RATE;
    } else if (balance < RATE1_MAX) {
        rate = POS_BAL_RATE1;
    } else if (balance < RATE2_MAX) {
        rate = POS_BAL_RATE2;
    } else {
        rate = POS_BAL_RATE3;
    }

    return rate;
}

// yearly_interest calculates the yearly interest for the provided balance.
double yearly_interest(double balance) {
    return balance * (interest_rate(balance) / 100);
}

// annual_balance_update calculates the annual balance update, taking into
// account the interest rate.
double annual_balance_update(double balance) {
    return balance + yearly_interest(balance);
}

// years_until_desired_balance calculates the minimum number of years required
// to reach the desired balance.
int years_until_desired_balance(double balance, double target_balance) {
    int count{0};
    while (balance < target_balance) {
        balance = annual_balance_update(balance);
        count++;
    }
    return count;
}
