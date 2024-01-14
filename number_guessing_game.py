import random

chosen_num = random.randint(1, 10)

while True:
    guess = int(input('Enter a random number between 1-10: '))
    if guess == chosen_num:
        print('U won\nCongratulations!!!')
        break
    else:
        print('Try Again!')