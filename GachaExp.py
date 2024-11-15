import random

def Gacha_game():
    print("Welcome to the Luck Game!")
    print("You will roll a number between 1 and 40.")
    print("If you roll a 40, you win! You have 10 tries.")
    input("Press Enter to start the game...")

    tries = 0
    max_tries = 10
    target_number = 40
    total_numbers = 140
    chance_of_winning = 1 / total_numbers * 100  


    print(f"\nYour chance of rolling a {target_number} is {chance_of_winning:.2f}%. Good luck!\n")
    
    while tries < max_tries:
        input(f"Try {tries + 1}: Press Enter to roll the dice...")
        roll = random.randint(1, total_numbers)
        print(f"You rolled a {roll} ")
        
        if roll == target_number:
            print("You won!!")
            break
        else:
            print("You lost, try again.\n")
        
        tries += 1
    
    if tries == max_tries:
        print("Game over! You've used all 10 tries.")

Gacha_game()
