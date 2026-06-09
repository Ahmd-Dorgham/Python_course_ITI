import random

def game():
    print("Guess a number from 1 to 100")
    num = random.randint(1, 100)
    attempts = 10
    played = []
    
    while attempts > 0:
        print("Tries left:", attempts)
        ans = input("Your guess: ")
        
        if ans.isdigit() == False:
            print("Please write a number")
            continue
            
        g = int(ans)
        
        if g < 1 or g > 100:
            print("Number must be 1 to 100")
            continue
            
        if g in played:
            print("You already wrote this number")
            continue
            
        played.append(g)
        attempts = attempts - 1
        
        if g == num:
            print("You win! The number is", num)
            break
        elif g < num:
            print("Larger!")
        else:
            print("Smaller!")
            
    if attempts == 0:
        print("You lost, game over")
        
    again = input("Play again? (y/n) ")
    if again == "y":
        game()

game()