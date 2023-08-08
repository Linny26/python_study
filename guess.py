# guess the number💖
print('Guess the number 0-10, you have 3 chance')
guess = 0
tries= 0
while guess != 10 and tries < 3 :
   guess = int(input('Guess the number: '))
   tries = tries + 1

if guess != 10:
   print('You ran out of tries')
else:
  print('You got it!')
