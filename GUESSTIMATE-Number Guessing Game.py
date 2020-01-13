import random

winning_number = random.randrange(0,10)
guess = 1
guessing_number = int(input("Guess a number b/w 1-10: "))
game_over = False

while not game_over:
        if winning_number == guessing_number:
            print(f"YOU WIN, in {guess} chance(s) !!!!")
            game_over = True

        else:
            if guessing_number > winning_number:
                print("Too High !")
                
            else:
                print("Too Low !")

            #DRY - don't repeat yourself  
            guess += 1
            guessing_number = int(input("Guess again: "))

                
