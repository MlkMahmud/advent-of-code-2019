def parse_input(filename):
  with open(filename) as file:
    return list(file.read().strip())


def get_layers(image, width, height):
  size = width * height
  layers = []
  for i in range(0, len(image), size):
    layers.append(image[i:i + size])
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

def decode_image(layers):
  decoded_image = layers[0]
  for x in range(1, len(layers)):
    layer = layers[x]
    for i in range(len(layer)):
      if decoded_image[i] == '2' and layer[i] in '10':
        decoded_image[i] = layer[i]
  return decoded_image


def print_image(image, width):
  for i in range(len(image)):
    char = image[i]
    if char == '0':
      image[i] = " "
    else:
      image[i] = '#'
  for x in range(0, len(image), width):
    print("".join(image[x: x + width]))

image = parse_input("input.txt")
layers = get_layers(image, 25, 6)
min_zeros = layer_with_fewest_zeros(layers)
print(f"Part One: {calculate(min_zeros)}")
print_image(decode_image(layers), 25)
