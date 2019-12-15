def parse_input(input):
  output = {}
  with open(input) as file:
    for line in file:
      a, b = line.strip().split(')')
      output[b] = a
  return output


def calculate_orbits(map):
  orbits = 0
  for key in map:
    while key in map:
      orbits += 1
      key = map[key]
  return orbits


    
def calculate_orbital_transfers(map):
  santa = map['SAN']
  you = map['YOU']
  path = {}
  your_moves = 0
  santas_moves = 0
  
  while you in map:
    you = map[you]
    your_moves += 1
    path[you] = your_moves
  
  while santa not in path:
    santa = map[santa]
    santas_moves += 1
  return santas_moves + path[santa]

    



map = parse_input("06/input.txt")
print(f"Part One: {calculate_orbits(map)}")
print(f"Part Two: {calculate_orbital_transfers(map)}")
