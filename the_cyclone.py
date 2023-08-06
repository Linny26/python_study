#cyclone 💖
height = int(input('How high are you?' ))
credits = int(input('How many credits do you have?' ))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif credits >= 10 and height < 137:
  print('You are not tall enough')
elif height >= 137 and credits < 10:
  print('You do not have enough credits')
else:
  print('You are not tall enough and you do not have enough credits')
