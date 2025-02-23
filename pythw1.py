#standard initilization comment
import random

#Simple function that asks the user to input two numbers, specifying that the 2nd must be larger than the first.
#Then selects and prints a random number from the range between the numbers the user input.

def random_function():
    print("Welcome to Random! Please pick a number: ")
    wowitsnum = int(input())
    print("Now please pick a second number that is LARGER than the first one you picked!: ")
    wownumagain = int(input())
    
    if wownumagain < wowitsnum:
        print("Oops! The second number must be larger than the first one.")
        return random_function()
    elif wownumagain == wowitsnum:
        print("NO THAT IS INCORRECT, PEBKAC")
        return random_function()  
    else:
        print("Wow, well done! Loading your prize...")
        random_num = random.randint(wowitsnum, wownumagain)
        print(f"Your number is {random_num}!")
        print("Try again? (y,n)")
        print("Hahaha.. we are on a strict budget, that feature has not and will not be implemented. Sorry!")
        print("Thanks for playing!")

random_function()