def convertInputToIntList(input):
  with open(input, "r") as file:
    return  [int(x) for x in file.read().strip().split(',')]

def resetComputerMemory(input, noun, verb):
  program = list.copy(input)
  program[1] = noun
  program[2] = verb
  return program
  
def restoreProgram(noun, verb):
  program = resetComputerMemory(convertInputToIntList("02/input.txt"), noun, verb)
  
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
      
  return program[0]

def findNounAndVerb(target):
  for noun in range(100):
    for verb in range(100):
      output = restoreProgram(noun, verb)
      if output == target:
        return f"Noun: {noun}, Verb: {verb}"
  return ""

print(restoreProgram(12, 2))
print(findNounAndVerb(19690720))
