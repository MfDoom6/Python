import random

def luck_game():
    tries = 0
    max_tries = 10
    target_number = 40
    total_numbers = 40
    chance_of_winning = 1 / total_numbers * 100  
    
    print(f"Welcome to the Luck Game! Your chance of rolling a {target_number} is {chance_of_winning:.2f}%.")
    print(f"You have {max_tries} tries to roll a {target_number} and win!\n")
    
    while tries < max_tries:
        roll = random.randint(1, total_numbers)
        print(f"Try {tries + 1}: You rolled a {roll}.")
        
        if roll == target_number:
            print("You won!!")
            break
        else:
            print("You lost, try again.")
        
        tries += 1
    
    if tries == max_tries:
        print("Game over! You've used all 10 tries.")

luck_game()
