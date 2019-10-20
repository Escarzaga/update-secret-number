import random
import json
import datetime


secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

name = input("What's your name?: ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

sorted_score_list = sorted(score_list, key=lambda x: x['attempts'])[:3]

for score_dict in sorted_score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".\
        format(score_dict.get("User name"), str(score_dict.get("attempts")), score_dict.get("date"),
        score_dict.get("secret_number"), score_dict.get("Unsuccessful guesses"))
    print(score_text)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1        # attempts = attempts + 1

    if guess == secret:
        current_time = str(datetime.datetime.now())
        score_data = {"User name": name, "secret_number": secret, "attempts": attempts,
                      "Unsuccessful guesses": wrong_guesses, "date": current_time}
        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            b = json.dumps(score_list)
            score_file.write(b)

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print(current_time)
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)