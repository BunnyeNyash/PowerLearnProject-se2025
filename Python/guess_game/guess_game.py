import random 
import time


guess = random.randint(2, 9)

TRIALS = 3
count_trial = 0

# Display game rules
print("I am thinking of a number between 1 and 10")
print("can you guess it? you have 3 tries")



while count_trial < TRIALS:
    # get input from the user
    user_guess = int(input(("Enter your guess, a number from 1 to 10: ")))

    # try again if guess is wrong and exit if out of tries
    if user_guess == guess:
        print("You guessed right! Kudos!")
        break
    elif user_guess > guess:
        print("Wrong guess! Try a lower value")
    elif user_guess < guess:
        print("Wrong guess! Try a higher value")

    count_trial += 1
        
# If user runs out of attempts
if count_trial == TRIALS and user_guess != guess:
    print("You're out of guessing chances. The number was", guess)
    time.sleep(2)
    exit()
            

