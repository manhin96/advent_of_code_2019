import math

def mass_fuel_calculator(input):
    return math.floor(input / 3) - 2

# Main method

filepath = "inputList"
totalFuel = 0

with open(filepath) as fp:
    for line in fp:
        totalFuel += mass_fuel_calculator(int(line))

print(int(totalFuel))