def calculateFuelRequirement(mass):
  return (mass // 3) - 2


def calculateTotalFuelRequired(input, fn):
  totalFuelRequired = 0
  with open(input, 'r') as file:
    for line in file:
      mass = int(line.strip())
      totalFuelRequired += fn(mass)
  return totalFuelRequired

print(calculateTotalFuelRequired('01/input.txt', calculateFuelRequirement))
