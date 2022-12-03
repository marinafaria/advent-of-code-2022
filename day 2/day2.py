file = open("input.txt", "r").read()

file_splitted = file.split(' ')
shapes = []

for i, line in enumerate(file_splitted):
  splitted_line =  line.split('\n')
  shapes.append(splitted_line[0])
  if len(splitted_line) > 1:
    shapes.append(splitted_line[1])

while('' in shapes):
    shapes.remove('')

def getScore():
  total_score = 0
  for i, line in enumerate(shapes):
    score = 0
    if i % 2 == 0 :
      if line == 'A': 
        player_one_answer = answer[0] 
      if line == 'B': 
        player_one_answer = answer[1] 
      if line == 'C': 
        player_one_answer = answer[2] 
    else:
      if line == 'X': 
        score = shape_score[0] + player_one_answer[0] 
      if line == 'Y': 
        score = shape_score[1] + player_one_answer[1] 
      if line == 'Z': 
        score = shape_score[2] + player_one_answer[2] 
      total_score = total_score + score
  return total_score

# Part One
answer = []
answer_A =[3, 6, 0]
answer_B = [0, 3, 6]
answer_C = [6, 0, 3]
answer.append(answer_A)
answer.append(answer_B)
answer.append(answer_C)
shape_score = [1, 2, 3] 

print('The score for the first strategy guide is', getScore())

# Part Two
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
answer = []
answer_A =[3, 1, 2]
answer_B = [1, 2, 3]
answer_C = [2, 3, 1]
answer.append(answer_A)
answer.append(answer_B)
answer.append(answer_C)
shape_score = [0, 3, 6]
print('The score for the second strategy guide is', getScore())
