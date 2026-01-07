def calculate_co2(units_kwh):
    emission_factor = 0.82  # kg CO2 per kWh (India average)
    return units_kwh * emission_factor
