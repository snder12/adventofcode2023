import sys

D = open(sys.argv[1]).read().strip()

sum_problem_2 = 0

for line in D.split('\n'):
  problem2_digits = []

  for index, character in enumerate(line):
    if character.isdigit():
      problem2_digits.append(character)

    for value, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[index:].startswith(word):
        problem2_digits.append(str(value+1))
  
  sum_problem_2 += int(problem2_digits[0] + problem2_digits[-1])
  
print(sum_problem_2) 
