def convert_input_to_list(input):
  with open(input, "r") as file:
    return  [int(x) for x in file.read().strip().split(',')]

def reset_computer_memory(input, noun, verb):
  program = list.copy(input)
  program[1] = noun
  program[2] = verb
  return program
  
def restore_program(noun, verb):
  program = reset_computer_memory(convert_input_to_list("02/input.txt"), noun, verb)
  
  for i in range(0, len(program), 4):
    opcode = program[i]
    if opcode == 99:
      break
    else:
      input_a = program[i + 1]
      input_b = program[i + 2]
      output = program[i + 3]
      if opcode == 1:
        program[output] = program[input_a] + program[input_b]
      elif opcode == 2:
        program[output] = program[input_a] * program[input_b]
      else:
        continue
      
  return program[0]

def find_noun_and_verb(target):
  for noun in range(100):
    for verb in range(100):
      output = restore_program(noun, verb)
      if output == target:
        return f"Noun: {noun}, Verb: {verb}"
  return ""

print(restore_program(12, 2))
print(find_noun_and_verb(19690720))
