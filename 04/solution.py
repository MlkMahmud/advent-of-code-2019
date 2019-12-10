def parseInput(input):
  return [int(x) for x in input.split('-')]

def possiblePassswordCombinations(start, stop):
  possibleCombinations = []
  for number in range(start, stop):
    combination = str(number)
    if list(combination) == sorted(combination) and len(combination) != len(set(combination)):
      possibleCombinations.append(combination)
  
  return possibleCombinations

def newPossiblePasswordCombinations(passwords):
  possibleCombinations = 0
  for password in passwords:
    for digit in set(password):
      if password.count(digit) == 2:
        possibleCombinations += 1
        break
  
  return possibleCombinations

start, stop = parseInput('246540-787419')
passwords = possiblePassswordCombinations(start, stop)
print(f"Possible Password Combinations Part 1: {len(passwords)}")
print(f"Possible Password Combinations Part 2: {newPossiblePasswordCombinations(passwords)}")

