import random


def play_high_low():
    """Plays a game of high-low"""
    num_rounds = int(input("How many rounds do you want to play?"))
    your_score = 0
    computer_score = 0
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number is {your_number}")
        while True:
            guess = input("Is your number higher or lower than the computer's?(higher/lower)").lower()
            if guess in ("higher", "lower"):
                break
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")
        if (your_number > computer_number and guess == "higher") or \
           (your_number < computer_number and guess == "lower"):
            print("You guessed it correctly!")
            your_score += 1
        else:
            print("You guessed it incorrectly.")
            computer_score += 1
    print("\nGame over!")
    print(f"Your score: {your_score}")
    print(f"Computer's score: {computer_score}")
    if your_score > computer_score:
        print("You won!")
    elif your_score < computer_score:
        print("The computer won.")
    else:
        print("Its a tie!")
play_high_low()