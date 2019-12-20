def parse_input(filename):
  with open(filename) as file:
    return [int(x) for x in file.read().strip().split(',')]


def get_codes(code):
  code = str(code).zfill(5)
  return [int(code[-2:]), int(code[-3]), int(code[-4]), int(code[-5])]

def get_param(program, mode, index, base):
  if mode == 1:
    param = index
  elif mode == 0:
    param = program[index]
  else:
    param = program[index] + base
  return param

def run_diagnostics(program, input):
  index = 0
  diagnostic_code = []
  relative_base = 0
  while True:
    opcode, mode_a, mode_b, mode_c = get_codes(program[index])

    if opcode == 99:
      break

    else:
      param_a = get_param(program, mode_a, index + 1, relative_base)
      param_b = get_param(program, mode_b, index + 2, relative_base)
      param_c = get_param(program, mode_c, index + 3, relative_base)

      if opcode == 1:
        program[param_c] = program[param_a] + program[param_b]
        index += 4

      elif opcode == 2:
        program[param_c] = program[param_a] * program[param_b]
        index += 4

      elif opcode == 3:
        program[param_a] = input
        index += 2

      elif opcode == 4:
        diagnostic_code.append(program[param_a])
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
          program[param_c] = 1
        else:
          program[param_c] = 0
        index += 4

      elif opcode == 8:
        if program[param_a] == program[param_b]:
          program[param_c] = 1
        else:
          program[param_c] = 0
        index += 4
      
      elif opcode == 9:
        relative_base += program[param_a]
        index += 2

  return diagnostic_code

program = parse_input("input.txt") + [0] * 500
print(f"Part One: {run_diagnostics(program, 1)}")
print(f"Part Two: {run_diagnostics(program, 2)}")
