import random

#user guess
def user_guess(x):
    random_number = random.randint(1,10)
    guess = 0
    print(random_number)
    while guess != random_number:
        guess = int(input("Guess the no.: "))

    print(f"You have guessed the right no. {random_number}")

#computer guess
def computer_guess(x):
    low = 1
    high = x
    ans = ''
    while ans != 'c':    
        random_num = random.randint(low, high)
        if low == high:
            ans = input(f"Is the guess {random_num} correct(c) or too low(l) or too high(h)")
        else:
            ans = input(f"Is the guess {random_num} correct(c) or too low(l) or too high(h)")
            if ans == "l":
                low = random_num + 1
            elif ans == "h":
                high = random_num - 1
    
    print(f"COngrats you have guessed the right no. {random_num}")

user_guess(10)
computer_guess(10)
    

