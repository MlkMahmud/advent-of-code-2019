def parse_input(filename):
  with open(filename) as file:
    return [int(x) for x in file.read().strip().split(',')]

def get_codes(code):
  code = str(code).zfill(4)
  return [int(code[-2:]), int(code[-3]), int(code[-4])]

def run_diagnostics(program, input):
  index = 0
  while True:
    opcode, mode_a, mode_b = get_codes(program[index])

    if opcode == 99:
      break
    
    else:
      param_a = index + 1 if mode_a == 1 else program[index + 1]
      param_b = index + 2 if mode_b == 1 else program[index + 2]

      if opcode == 1:
        program[program[index + 3]] = program[param_a] + program[param_b]
        index += 4
    
      elif opcode == 2:
        program[program[index + 3]] = program[param_a] * program[param_b]
        index += 4
    
      elif opcode == 3:
        program[program[index + 1]] = input
        index += 2
    
      elif opcode == 4:
        program[0] = program[program[index + 1]]
        index += 2
      
      elif opcode == 5:
        if program[param_a] != 0:
          index = program[param_b]
        else:
          index += 3
      
      elif opcode == 6:
        if program[param_a] == 0:
          index = program[param_b]
        else:
          index += 3
      
      elif opcode == 7:
        if program[param_a] < program[param_b]:
          program[program[index + 3]] = 1
        else:
          program[program[index + 3]] = 0
        index += 4
      
      elif opcode == 8:
        if program[param_a] == program[param_b]:
          program[program[index + 3]] = 1
        else:
          program[program[index + 3]] = 0
        index += 4

  return program[0]


program = parse_input("input.txt")
print(f"Part One: {run_diagnostics(program[:], 1)}")
print(f"Part Two: {run_diagnostics(program[:], 5)}")
