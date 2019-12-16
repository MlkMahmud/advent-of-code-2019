def parse_input(input):
  with open(input) as file:
    a,b = file.read().strip().split('\n')
    return [a.split(','), b.split(',')]

def get_coordinates(path):
  x = 0
  y = 0
  coordinates = []
  steps = 0
  moves = {}
  for point in path:
    direction = point[0]
    distance = int(point[1:])
    x_distance = 0
    y_distance = 0
    if direction == 'U':
      y_distance = 1
    
    elif direction == 'D':
      y_distance = -1
    
    elif direction == 'L':
      x_distance = -1
    
    elif direction == 'R':
      x_distance = 1
    else:
      pass
    
    for _ in range(distance):
      x += x_distance
      y += y_distance
      steps += 1
      coordinates.append((x, y))
      key = str(x) + str(y)
      if key not in moves:
        moves[key] = steps
  coordinates.insert(0, moves)
  return coordinates
      
def get_manhatthan_distance(a, b):
  overlaps = list(set(a[1:]) & set(b[1:]))
  return min([abs(a) + abs(b) for a, b in overlaps])


def calculate_fewest_steps(a, b):
  overlaps = list(set(a[1:]) & set(b[1:]))
  path_a = a[0]
  path_b = b[0]
  steps = []
  for x, y in overlaps:
    key = str(x) + str(y)
    if key in path_a and key in path_b:
      steps.append(path_a[key] + path_b[key])
  return min(steps)

a, b = parse_input("input.txt")
wire_a = get_coordinates(a)
wire_b = get_coordinates(b)
print(f"Part One: {get_manhatthan_distance(wire_a, wire_b)}")
print(f"Part Two: {calculate_fewest_steps(wire_a, wire_b)}")
