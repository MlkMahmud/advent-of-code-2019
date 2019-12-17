def parse_input(filename):
  with open(filename) as file:
    return list(file.read().strip())


def get_layers(image, width, height):
  step = width * height
  layers = []
  for i in range(0, len(image), step):
    layers.append(image[i:i + step])
  return layers

def layer_with_fewest_zeros(layers):
  output = min_zeros = None
  for layer in layers:
    zeros = layer.count('0')
    if not min_zeros or zeros < min_zeros:
      output = layer
      min_zeros = zeros
  return output

def calculate(layer):
  return layer.count('1') * layer.count('2')

image = parse_input("input.txt")
layers = get_layers(image, 25, 6)
min_zeros = layer_with_fewest_zeros(layers)
print(f"Part One: {calculate(min_zeros)}")
