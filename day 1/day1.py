file = open("input.txt", "r").read()

total_calories = file.split('\n\n')

for i, line in enumerate(total_calories):
  line = map(int,line.split('\n'))
  total_calories[i] = sum(line)

max = 0
for line in total_calories:
  if line > max:
    max = line

total_calories = sorted(total_calories, reverse=True)
top3_calories_sum = sum([total_calories[0],total_calories[1], total_calories[2]])

print('The Elf carrying the most Calories have', max, 'calories')
print('The top three Elves carrying the most Calories have', top3_calories_sum, 'calories in total')