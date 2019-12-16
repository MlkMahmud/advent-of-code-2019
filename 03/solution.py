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
      if (x, y) not in moves:
        moves[(x, y)] = steps
  coordinates.insert(0, moves)
  return coordinates
      
def get_manhatthan_distance(a, b):
  overlaps = list(set(a[1:]) & set(b[1:]))
  return min([abs(a) + abs(b) for a, b in overlaps])


def get_min_steps(a, b):
  overlaps = list(set(a[1:]) & set(b[1:]))
  path_a = a[0]
  path_b = b[0]
  min_steps = None
  for x, y in overlaps:
    key = (x, y)
    if key in path_a and key in path_b:
      steps = path_a[key] + path_b[key]
      if min_steps is None or steps < min_steps:
        min_steps = steps
  return min_steps

a, b = parse_input("input.txt")
wire_a = get_coordinates(a)
wire_b = get_coordinates(b)
print(f"Part One: {get_manhatthan_distance(wire_a, wire_b)}")
print(f"Part Two: {get_min_steps(wire_a, wire_b)}")
