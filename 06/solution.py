def parse_input(input):
  output = {}
  with open(input) as file:
    for line in file:
      a, b = line.strip().split(')')
      output[b] = a
  return output


def calculate_orbits(data):
  orbits = 0
  for key in data:
    while key in data:
      orbits += 1
      key = data[key]
  return orbits

  
  



data = parse_input("06/input.txt")
print(f"Part One: {calculate_orbits(data)}")
