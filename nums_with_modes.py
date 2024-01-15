import random

nums = random.randint(1, 50)

lives = 10
def easy(nums, live):
    while True:
        guess = int(input('Enter a number between 1-50 (remember you have 10 lives): '))
        if guess == nums:
            return "You Won!"
        elif guess < nums:
            live -= 1
            print('The number you entered is too low')
        elif guess > nums:
            live -= 1
            print('The number you entered is too big')
        
        if live == 0:
            return 'You Lost!'


nums = random.randint(1, 100)
lives = 5

def hard(nums, live):
    while True:
        guess = int(input('Enter a number between 1-100 (remember you have 5 lives): '))
        if guess == nums:
            return "You Won!"
        elif guess < nums:
            print('The number you entered is too low!')
            live -= 1
        elif guess > nums:
            print('The number you entered is too big (Thats what She said)')
            live -= 1
        if live == 0:
            return 'You Lost!'

user_in = int(input('There is two difficulty levels easy and hard press (1) to play the easy mode or press (2) to play the hard mode: '))
if user_in == 1:
    print(easy(nums, lives))
elif  user_in == 2:
    print(hard(nums, lives))
else:
    print('you entered a wrong input! run the program again!')