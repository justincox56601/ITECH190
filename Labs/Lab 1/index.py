message = "what is your name? "
print(message)
name = input()

welcome_message = f"welcome {name}"
print(welcome_message)

random_number = 7
guess_prompt = "Please guess a number between 1 and 10"
print(guess_prompt)
guess_number = int(input())

correct_message = "Congrats!!  you guessed the secret number."
wrong_message = "Sorry, that guess was incorrect."
if random_number == int(guess_number):
    print(correct_message)
else:
    print(wrong_message)

