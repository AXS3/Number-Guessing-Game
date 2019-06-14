import random
for x in range(10):
    z = random.randint(1,11)
print('Guess a number from 1 - 10')
if (z % 2) == 0:
   print('The Number Is Even')
else:
   print('The Number Is Odd')
if z < 5:
   print('The Number Is Smaller Than 5')
else:
   print('The Number Is Larger Than 5')
y = input('What Is The Number?')
if y == str(z):
    print('Correct')
else:
    print('Wrong')
print('The answer was ' + str(z))
