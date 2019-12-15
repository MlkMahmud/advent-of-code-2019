def parse_input(input):
  return [int(x) for x in input.split('-')]

def possible_passsword_combinations(start, stop):
  possible_combinations = []
  for number in range(start, stop):
    combination = str(number)
    if list(combination) == sorted(combination) and len(combination) != len(set(combination)):
      possible_combinations.append(combination)
  
  return possible_combinations

def new_possible_password_combinations(passwords):
  possible_combinations = 0
  for password in passwords:
    for digit in set(password):
      if password.count(digit) == 2:
        possible_combinations += 1
        break
  
  return possible_combinations

start, stop = parse_input('246540-787419')
passwords = possible_passsword_combinations(start, stop)
print(f"Possible Password Combinations Part 1: {len(passwords)}")
print(f"Possible Password Combinations Part 2: {new_possible_password_combinations(passwords)}")

