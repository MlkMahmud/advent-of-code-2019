def calculate_fuel_requirement(mass):
  return (mass // 3) - 2


def calculate_additional_fuel_requirement(fuel):
  additional_fuel = 0
  while True:
    fuel = calculate_fuel_requirement(fuel)
    if fuel < 1:
      break
    additional_fuel += fuel
  return additional_fuel


with open("input.txt") as file:
  fuel_requirement = 0
  additional_fuel_requirement = 0
  for line in file:
    mass = int(line.strip())
    fuel_requirement += calculate_fuel_requirement(mass)
    additional_fuel_requirement += calculate_additional_fuel_requirement(mass)
  print(f"Fuel Requirement: {fuel_requirement}\nAdditional Fuel Requirement: {additional_fuel_requirement}")
