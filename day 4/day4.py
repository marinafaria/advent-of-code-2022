result = 0

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
        if(pair_int[0] <= pair_int[2] and pair_int[1] >= pair_int[3]):
          print('entrei no if 1 com o par:', pair_int)
          result+=1
        elif(pair_int[0] >= pair_int[2] and pair_int[1] <= pair_int[3]):
          print('entrei no if 2 com o par:', pair_int)
          result+=1

print(result) 

# 14-38,14-14
# 2-10,3-55
# 36-90,36-46
# 9-97,8-87
# 75-92,51-92
# 6-82,1-83
# 21-79,29-80
# 26-66,27-27