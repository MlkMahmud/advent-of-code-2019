def parseInput(input):
  return [int(x) for x in input.split('-')]

def getPossiblePassswordCombinations(start, stop):
  possibleCombinations = 0
  for number in range(start, stop):
    combination = str(number)
    if list(combination) == sorted(combination) and len(combination) != len(set(combination)):
      possibleCombinations += 1
  
  return possibleCombinations


start, stop = parseInput('246540-787419')
print(f"Possible Password Combinations Part 1: {getPossiblePassswordCombinations(start, stop)}")


