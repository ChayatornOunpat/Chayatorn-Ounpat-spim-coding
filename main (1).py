str = input('please enter a value ')
strlist = list(str)
res = 0
for num in strlist:
  res = res + int(num)
print(res)