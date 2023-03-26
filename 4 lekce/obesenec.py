from pprint import pprint
import random


def main():
    words = load_words("C:\Programování\python-academy\čtvrtá lekce\words.txt")
    welcome()
    user_name = get_user_name()
    print(user_name)
    secrete_word = select_word(words)
    print(secrete_word)
    guessed_character_list = []
    show_state(secrete_word, guessed_character_list)
    pokusy = 10
    while pokusy:
        guessed_character = guess_char()
        guessed_character_list.append(guessed_character)
        state = show_state(secrete_word, guessed_character_list)
        print(f"Hráč {user_name} | {state} | zbývá ti {pokusy} pokusů  ")
        if "_" not in state:
            print(f"Vyhrál jsi! Zbylo ti {pokusy} pokusů")
            break
        pokusy -= 1

    if pokusy == 0:
        print("Prohrál jsi! amatére.")


def load_words(path):
    with open(path, "r") as file:
        word_list = file.readlines()
    clean_list = []
    for i in word_list:
        clean_list.append(i.rstrip("\n"))
    return clean_list


def welcome():
    pprint(""" Výtej v naší hře! budeš hádat slova""")


def get_user_name():
    name = input("Zadej své jméno:")
    return name


def select_word(words):
    return random.choice(words)


def show_state(secret, guessed_character=None):
    output = []
    for i in secret:
        if i in guessed_character:
            output.append(i)
        else:
            output.append("_")

    return output


def guess_char():
    character = input("Hadej písmeno:")
    return character


main()
