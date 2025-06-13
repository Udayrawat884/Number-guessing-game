import random

def numer_guessing_game():
    print("Welcom to the number guessing game i will guess a number between 1 to 100. And you have to guess the number")
    print("You 7 attemps to guess the number.")

    number_to_guess = random.randint(1, 100)
    attemps = 7

    while attemps > 0:
        try:
            guess = int(input(f"You have {attemps} attemps lestGive me the number from 1 to 100 you think i have guessed."))
        except ValueError:
            print("❌ Invalid Error. Plese Try again.")
            continue
        if guess < 1 and guess > 100:
            print("⚠️Please guess a number between 1 to 100")
        elif guess == number_to_guess:
            print(f"✅Correct guess. The number was {number_to_guess}")
            break
        elif guess > number_to_guess:
            print("⬆️To high")
        elif guess < number_to_guess:
            print("⬇️To low")

        attemps -=1
    else:
        print(f"You are out you attemps are over the number i guess was {number_to_guess}")

if __name__ == "__main__":
    numer_guessing_game()