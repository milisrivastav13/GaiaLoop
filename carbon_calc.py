import numpy as np

def calculate_carbon(transport, electricity, diet):
    """
    Simple carbon footprint calculator.
    transport: km traveled by car/public transport
    electricity: kWh used
    diet: 0 (vegan), 1 (vegetarian), 2 (non-veg)
    """
    transport_factor = 0.21   # kg CO2 per km
    electricity_factor = 0.92 # kg CO2 per kWh
    diet_factor = [2, 3.5, 5] # kg CO2 per day (vegan, veg, non-veg)
    
    total = transport*transport_factor + electricity*electricity_factor + diet_factor[diet]
    return round(total, 2)