def file_to_list(input):
  with open(input) as file:
    return file.read().strip().split('\n')
