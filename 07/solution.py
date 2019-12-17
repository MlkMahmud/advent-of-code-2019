from itertools import permutations

def parse_input(input):
  with open(input) as file:
    return [int(x) for x in file.read().strip().split(',')]

def get_codes(code):
  code = str(code).zfill(4)
  return [int(code[-2:]), int(code[-3]), int(code[-4])]


def run_diagnostics(program, phase, input):
  index = 0
  diagnostic_code = None
  input_count = 0
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
        program[program[index + 1]] = phase if input_count == 0 else input
        index += 2
        input_count += 1

      elif opcode == 4:
        diagnostic_code = program[program[index + 1]]
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
      else:
        break

  return diagnostic_code

def run_amplifier(program, phase_setting, input):
  for phase in phase_setting:
    input = run_diagnostics(program, phase, input)
  return input

def get_max_thruster_signal(program, phase_setting, fn):
  max_signal = None
  for phase in permutations(phase_setting):
    result = fn(program[:], phase, 0)
    if not max_signal or result > max_signal:
      max_signal = result
  return max_signal

program = parse_input("input.txt")
print(f"Part One: {get_max_thruster_signal(program, [0,1,2,3,4], run_amplifier)}")
