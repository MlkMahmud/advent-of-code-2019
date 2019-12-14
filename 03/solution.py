def parse_input(input):
  with open(input) as file:
    return file.read().strip().split('\n')
