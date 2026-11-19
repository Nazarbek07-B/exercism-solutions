EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time in minutes."""
    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining



def preparation_time_in_minutes(number_of_layers): 
    """Calculate the preparation time based on the number of layers."""
    preparation_time = PREPARATION_TIME*number_of_layers
    return preparation_time



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent preparing and baking the lasagna."""
    elapsed_time = elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    return elapsed_time



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
