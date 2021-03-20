from Player import Player


def get_positive_number(question):
    correct_input = False
    while not correct_input:
        try:
            number_to_return = int(input(question))
            if number_to_return <= 0:
                print("Skriv ett tal större än 0\n")
            else:
                correct_input = True
        except ValueError:
            print("Skriv ett heltal\n")
    return number_to_return


def main_game_loop(player_list, number_of_turns):
    number_of_players = len(player_list)
    print("\n")
    for turn_number in range(number_of_turns):
        forbidden_words = set()
        print(f"Omgång nummer {turn_number + 1}")
        print(f"{player_list[turn_number % number_of_players]} ska välja ord.")
        starting_word = str(input("Ord: "))
        forbidden_words.add(starting_word.lower())
        new_word = starting_word
        for mini_turn in range(number_of_players - 1):
            if mini_turn % 2 == 0:
                print(f"{player_list[mini_turn + 1]} har fått ordet {new_word}.")
                print("Skriv din ledtråd för ordet.")
                hint = input("Ledtråd: ")
            else:
                print(f"{player_list[mini_turn + 1]} har fått ledtråden {hint}.")
                print("Skriv din gissning.")
                new_word = input("Gissning: ")

        print("\n")


def create_player_list(number_of_players):
    player_list = []
    for i in range(number_of_players):
        name = input(f"Namn för spelar nummer {i + 1}: ")
        player_list.append(Player(name))
    return player_list


def main():
    print("TODO: SPELREGLER SKA IN HÄR SEN")
    print("Hur många spelar ska spela?")
    number_of_players = get_positive_number("Antal spelare: ")
    player_list = create_player_list(number_of_players)
    number_of_turns = get_positive_number("Antal omgångar: ")
    main_game_loop(player_list, number_of_turns)


if __name__ == '__main__':
    main()
