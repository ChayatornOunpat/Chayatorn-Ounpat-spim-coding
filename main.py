str_1 = input('please enter your first word ')
str_2 = input('please enter your second word ')


res = (f'{str_1}{str_2}')
if len(res) < 51:
  print(res)
else:
  print('limit is at 50 character')