import random 

def guessing_game():
    print("This is the Guessing Game. You have 5 attempts to guess the random number between 0 and 10.")

    while True:
        random_number = random.randint(0, 10)
        tries = 0
        max_tries = 5  

        while tries < max_tries:
            guess = int(input(f"Attempt {tries + 1}/{max_tries}: Enter your guess: "))
            tries += 1

            if guess == random_number:
                print(f"Congratulations! did it! {random_number} correctly in {tries} tries.")
                break
            else:
                if tries < max_tries:
                    print("Incorrect guess, try again.")
                else:
                    print(f"You've run out of tries! The correct number was {random_number}.")

        
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again in ('y', 'n'):
                break
            else:
                print("Invalid input. Please enter 'y' to continue or 'n' to stop.")

        if play_again == 'n':
            print("Thanks for playing!")
            break
 
guessing_game()
print ("completed by Benjamin Harrison")
