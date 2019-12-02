import math

def mass_fuel_calculator(input, totalSum=0):
    calculatedValue = math.floor(input / 3) - 2
    if calculatedValue <= 0:
        return totalSum
    else:
        return mass_fuel_calculator(calculatedValue, totalSum + calculatedValue)

# Main method
if __name__ == '__main__':
    filepath = "inputList"
    totalFuel = 0

    with open(filepath) as fp:
        for line in fp:
            totalFuel += mass_fuel_calculator(int(line))

    print(int(totalFuel))
