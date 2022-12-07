resultPartOne = 0
resultPartTwo = 0

with open('input.txt') as file: 
  for line in file:
    pair = line.split(',')
    for i, element in enumerate(pair):
      if(i%2 == 0):
        pair_int = []
      element = element.split('-')
      for x in element:
        pair_int.append(eval(x))
      if(len(pair_int) == 4):
        # Part One
        if(pair_int[0] <= pair_int[2] and pair_int[1] >= pair_int[3]):
          resultPartOne+=1
        elif(pair_int[0] >= pair_int[2] and pair_int[1] <= pair_int[3]):
          resultPartOne+=1
        # Part Two
        if(pair_int[1] >= pair_int[2] and pair_int[0] <= pair_int[3]):
          print('entrei no if com o par:', pair_int)
          resultPartTwo+=1

print(resultPartOne) 
print(resultPartTwo) 