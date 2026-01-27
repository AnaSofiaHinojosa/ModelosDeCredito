from random import randint

def generate_number():
    return randint(1, 100)

def guess():
    return int(input("Number: "))

def check_win(secret, player_guess):
    return secret == player_guess


def play_game():
    secret_number = generate_number()
    lives = 5

    print("Guess the number between 1 and 100")
    print(f"You have {lives} lives.")

    while lives > 0:
        player_guess = guess()

        if check_win(secret_number, player_guess):
            print("🎉 You won!")
            return
        else:
            lives -= 1
            if secret_number > player_guess:
                print(f"Wrong guess, your number was too low! Lives remaining: {lives}")
            elif secret_number < player_guess:
                print(f"Wrong guess, your number was too high! Lives remaining: {lives}")

    print(f"💀 Game over! The number was {secret_number}")

play_game()
