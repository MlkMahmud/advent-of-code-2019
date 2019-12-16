def parse_input(input):
  with open(input) as file:
    a,b = file.read().strip().split('\n')
    return [a.split(','), b.split(',')]

def get_coordinates(path):
  x = 0
  y = 0
  coordinates = []
  for point in path:
    direction = point[0]
    steps = int(point[1:])
    x_counter = 0
    y_counter = 0
    if direction == 'U':
      y_counter = 1
    
    elif direction == 'D':
      y_counter = -1
    
    elif direction == 'L':
      x_counter = -1
    
    elif direction == 'R':
      x_counter = 1
    else:
      pass
    
    for _ in range(steps):
      x += x_counter
      y += y_counter
      coordinates.append((x, y))
  
  return coordinates
      
def get_manhatthan_distance(a, b):
  overlaps = list(set(a) & set(b))
  return min([abs(a) + abs(b) for a, b in overlaps])


wire_a, wire_b = parse_input("input.txt")
print(f"Part One: {get_manhatthan_distance(get_coordinates(wire_a), get_coordinates(wire_b))}")


