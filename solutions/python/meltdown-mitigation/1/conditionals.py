"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False
    

def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage_value = ((voltage * current) / theoretical_max_power) * 100
    if percentage_value >= 80:
        return "green"
    elif percentage_value >= 60:
        return "orange"
    elif percentage_value >= 30:
        return "red"
    else:
        return "black"
   

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    if product < (threshold * 90) / 100:
        return "LOW"
    elif product >= (threshold * 90) / 100 and product <= (threshold * 110) / 100:
        return "NORMAL"
    else:
        return "DANGER"