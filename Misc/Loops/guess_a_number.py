#Reference : https://www.linkedin.com/pulse/learn-looping-python-fun-text-based-games-doug-purcell/
import random

# random_num is the number in range 1 ... 100

# tries keep count of how many guesses player makes

tries, random_num = 0, random.randint(1, 100)

while True:

  print('Guess a number in the range of 1-100')

  your_guess = int(input())

  if your_guess > random_num:

    print('{} is greater than the random number X'.

       format(your_guess))

    tries += 1

  elif your_guess < random_num:

    print('{} is less than the random number X'.

       format(your_guess))

    tries += 1

  else:

    print('Congrats! {} is equal to the random number '

       '{}.'.format(your_guess, random_num))

    tries += 1

    print('It took you {} tries'.format(tries))

    break
