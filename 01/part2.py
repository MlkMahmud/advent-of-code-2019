from part1 import calculateFuelRequirement, calculateTotalFuelRequired


def calculateAdditionalFuelRequirement(fuel):
  additionalFuel = 0 
  while True:
    fuel = calculateFuelRequirement(fuel)
    if fuel < 1:
      break
    additionalFuel += fuel
  return additionalFuel

print(calculateTotalFuelRequired('01/input.txt', calculateAdditionalFuelRequirement))


