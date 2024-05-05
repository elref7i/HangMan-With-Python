import random
from hangmanLogo import word_list,logo,stages
chosen_word = random.choice(word_list)
print(logo)
list_th = []
th = "_"
for i in chosen_word:
    list_th.append(th)
# حلى
lives = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ?!").lower()
    for index,letter in enumerate(chosen_word):
        if letter == guess:
            list_th[index] = guess
    list_string = "".join(list_th)
    if guess in list_th:
        print(f"{guess} is alredy here Try again ☺ ")
    if guess not in chosen_word:
        lives -= 1
        print(f"Number of attempts = {lives}")
        if lives == 0:
            end_game = True
            print(f"You Lose")
    print(list_string)
    if "_" not in list_th:
        print("Win")
        end_game = True
    print(stages[lives])


