import random


def main():
    ordlista = []
    # Gets the word-list
    f = open("ordlista.txt", "r")
    for i in f:
        ordlista.append(f.readline())
    f.close()
    # Removes \n from each word
    for i in range(len(ordlista)):
        ordlista[i] = ordlista[i].strip("\n")

    chosen_word = random.choice(ordlista)
    number_of_guesses = 1
    correct_guess = False
    print("Gissa vilket ord jag tänker på!")
    while not correct_guess:
        guess = input("Gissning: ").lower().strip()
        if guess == chosen_word:
            print("Helt rätt! Ordet var", chosen_word)
            print("Grattis!!")
            print("Det tog", number_of_guesses, "försök")
            correct_guess = True
        elif guess < chosen_word:
            print("Fel. Ordet ligger senare i alfabetisk ordning")
        elif guess > chosen_word:
            print("Fel. Ordet ligger tidigare i alfabetisk ordning")

        number_of_guesses += 1


main()
