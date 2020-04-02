import random


def pick_capital():
    capitals = ['BUDAPEST', 'VATICAN', 'PRAGUE', 'BERLIN', 'PARIS', 'NEW YORK']
    return random.choice(capitals)



def get_hashed(word):
    hashed = ""
    for letter in word:
        hashed = hashed + " " if letter == " " else hashed + "_"
    return hashed


def uncover(hashed_password, password, letter):
    copy = list(hashed_password)
    for i in range(len(password)):
        if password[i] == letter:
            copy[i] = letter
    return "".join(copy)


def update(used_letters, letter):
    used_letters.append(letter)
    return used_letters


def is_win(hashed_password, password):
    return hashed_password == password


def is_loose(life_points):
    return life_points < 1


def get_input():
    while True:
        letter = input("Give me a letter: ")
        if letter.isalpha() and len(letter) == 1:
            return letter.upper()
        else:
            print("Give me a valid letter!")


def main():
    used_letters = []
    life_points = 5
    capital = pick_capital()
    hashed = get_hashed(capital)
    while not is_loose(life_points):
        print(f'Used letters: {used_letters}')
        print(f"You have {life_points} lives left!")
        print(hashed)
        letter = get_input()
        if letter not in used_letters:
            used_letters = update(used_letters, letter)
            if letter in capital:
                hashed = uncover(hashed, capital, letter)
            else:
                life_points -= 1
        else:
            print("This letter is already used!")
        if is_win(hashed, capital):
            print(f"The word was: {capital}  \n Congratulations! You Win!")
            break
    if life_points == 0:
        print(f'The word was {capital} !')
        print("You lose!")


if __name__ == '__main__':
    main()
