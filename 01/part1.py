def calculateFuelRequirement(mass):
  return (mass // 3) - 2


with open('01/input.txt', 'r') as file:
  totalFuelRequired = 0
  for line in file:
    mass = int(line.strip())
    totalFuelRequired += calculateFuelRequirement(mass)
  print(totalFuelRequired)
