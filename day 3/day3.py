with open('input.txt') as file:
  rucksacks = file.readlines()

def getPriorityNumber(letter):
  letter = ord(letter)
  if letter > 96:
    return letter - 96
  else:
    return letter - 38

# Part One
priority_sum = 0
for rucksack in rucksacks:
  first_compartment = rucksack[:len(rucksack)//2]
  second_compartment = rucksack[len(rucksack)//2:]
  actual_char = ''
  for char in first_compartment:
      if (second_compartment.find(char) != -1) and (char != actual_char):
        actual_char = char
        priority_sum+= getPriorityNumber(char)

print('The sum of the priorities of the rucksacks is', priority_sum)

# Part Two
def isCharSticker(group_rucksacks, char):
  for r in group_rucksacks:
    if r.find(char) == -1:
      return False
  return True

priorities_sum = 0
group_rucksacks = []
for i, rucksack in enumerate(rucksacks):
  group_rucksacks .append(rucksack)

  if((i+1) % 3 == 0): 
    actual_char = ''
    for char in group_rucksacks[0]:
        if (isCharSticker(group_rucksacks, char)) and (char != actual_char) and (char != '\n'):
          actual_char = char
          priorities_sum+= getPriorityNumber(char)
    group_rucksacks = []

print('The sum of the priorities of the badges is', priorities_sum)