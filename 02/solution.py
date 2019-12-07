
def convertInputToIntList(input):
  with open(input, "r") as file:
    return  [int(x) for x in file.read().strip().split(',')]

def resetComputerMemory(input):
  program = input
  program[1] = 12
  program[2] = 2
  return program
  
def restoreProgram():
  program = resetComputerMemory(convertInputToIntList("02/input.txt"))
  
  for i in range(0, len(program), 4):
    opcode = program[i]
    if opcode == 99:
      break
    else:
      inputA = program[i + 1]
      inputB = program[i + 2]
      output = program[i + 3]
      if opcode == 1:
        program[output] = program[inputA] + program[inputB]
      elif opcode == 2:
        program[output] = program[inputA] * program[inputB]
      else:
        continue

  return program


print(restoreProgram())
