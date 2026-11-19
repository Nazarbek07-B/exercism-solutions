"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

    
"""This function calculates and returns the (estimated) value of the exchanged currency."""


def get_change(budget, exchanging_value):
    return budget - exchanging_value

# This function calculates and returns the amount of money left over from the budget after an exchange.



def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills
    """This function calculates and returns the total value of the bills (excluding fractional amounts).

    """

def get_number_of_bills(amount, denomination):
    return amount // denomination
    """This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts"""


def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    """This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination"""


def exchangeable_value(budget, exchange_rate, spread, denomination):
    effective_exchange_rate = (exchange_rate * spread/100)+exchange_rate
    exchanged = exchange_money(budget, effective_exchange_rate)
    number_of_bills = exchanged//denomination
    return get_value_of_bills(denomination, number_of_bills)
    
    
"""This function calculates and returns the maximum value of the new currency after determining the exchange rate plus the spread."""


