"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# 40 min per lasagna
EXPECTED_BAKE_TIME = 40
# two minutes per layer
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate bake time remaining.

    :param elapased_bake_time: int - time spent already in oven.
    :return: int - remaining time in oven based off of EXPECTED_BAKE_TIME

    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - prepartion time based off of number of layers and PREPARATION_TIME per layer

    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed time in minutes.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - time spend in kitchen, prep time plus elapsed_bake_time.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
