import random
def guessing_game():
    print("=== WELLCOME TO AWR GUESSING GAME ===")
    print("=== GUESS THE NUMBER BETWEEN 1 AND 100 === \n")

    screat_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = int(input("ENTER YOUR GUESS NUMBER :"))
            attempts += 1

            if guess > screat_number:
                print("Too high! Please Try again? \n")
            elif guess < screat_number:
                print("Too low! Please Try again? \n")
            else:
                print(f"👍 Correct! you guess the number({screat_number}) in ({attempts})attempts!")
                break
        except ValueError:
            print("❌ Please enter a number! \n")

    print("Thanks for playing!")

guessing_game()
