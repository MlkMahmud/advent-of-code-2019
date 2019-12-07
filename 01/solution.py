def calculateFuelRequirement(mass):
  return (mass // 3) - 2


def calculateAdditionalFuelRequirement(fuel):
  additionalFuel = 0
  while True:
    fuel = calculateFuelRequirement(fuel)
    if fuel < 1:
      break
    additionalFuel += fuel
  return additionalFuel


with open("01/input.txt", "r") as file:
  fuelRequirement = 0
  additionalFuelRequirement = 0
  for line in file:
    mass = int(line.strip())
    fuelRequirement += calculateFuelRequirement(mass)
    additionalFuelRequirement += calculateAdditionalFuelRequirement(mass)
  print(f"Fuel Requirement: {fuelRequirement}\nAdditional Fuel Requirement: {additionalFuelRequirement}")
