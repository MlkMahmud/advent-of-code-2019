moons = [
  {
    'pos': [17, -12, 13],
    'vel': [0, 0, 0]
  },
  {
    'pos': [2,1,1],
    'vel': [0, 0, 0]
  },
  {
    'pos': [-1, -17, 7],
    'vel': [0, 0, 0]
  },
  {
      'pos': [12, -14, 18],
      'vel': [0, 0, 0]
  },
]

def apply_gravity(moon_a, moon_b):
  for i in range(3):
    if moon_a['pos'][i] > moon_b['pos'][i]:
      moon_a['vel'][i] -= 1
      moon_b['vel'][i] += 1
    elif moon_a['pos'][i] < moon_b['pos'][i]:
      moon_a['vel'][i] += 1
      moon_b['vel'][i] -= 1
    else:
      pass

def apply_velocity(moons):
  for moon in moons:
    for i in range(3):
      moon['pos'][i] += moon['vel'][i]


def calculate_total_energy(moons):
  total_energy = 0
  for moon in moons:
    total_energy += sum(list(map(lambda x: abs(x), moon['vel']))) * sum(list(map(lambda x : abs(x), moon['pos'])))
  return total_energy


def simulate_time_steps(moons, steps=0):
  step = 0
  while step < steps:
    for i in range(4):
      for j in range(i + 1, 4):
        apply_gravity(moons[i], moons[j])
    
    apply_velocity(moons)
    step += 1
  return calculate_total_energy(moons)


print(f"Part One: {simulate_time_steps(moons, 1000)}")
