# Control Flow
isRaining = input('Is it raining?')
isRaining = isRaining.lower()
if isRaining == 'yes' or isRaining == 'it is' or isRaining == 'yeah':
  print('It is raining outside.')
elif isRaining == 'no':
  print('It is not raining right now.')
else:
  print('Your guess is as good as mine')

