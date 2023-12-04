import sys

D = open(sys.argv[1]).read().strip()

sum_problem_1 = 0

for line in D.split('\n'):
  problem1_digits = []

  for index, character in enumerate(line):
    if character.isdigit():
      problem1_digits.append(character)
  
  sum_problem_1 += int(problem1_digits[0] + problem1_digits[-1])
  
print(sum_problem_1) 
