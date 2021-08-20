var_1 = int(input('please enter the first value'))
var_2 = int(input('please enter the second value'))
var_3 = int(input('please enter the third value'))


def cubed(num):
  return num*num*num


def squared(num):
  return num*num


num_1 = cubed(var_1)
num_2 = squared(var_2)
num_3 = var_3
print(num_1 + num_2 + num_3)