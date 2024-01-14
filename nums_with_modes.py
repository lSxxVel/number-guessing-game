import random

nums = random.randint(1, 50)

lives = 10
print(nums)
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

print(easy(nums, lives))

# FUCK ELECTRICITY