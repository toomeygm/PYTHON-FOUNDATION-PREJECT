print("hi one")

import random  # This line imports the random module, which allows generating random numbers.


def get_player_names():  # to customise the game with a set of values(here the players' names), we've used a tuple
    player1name = input("Hi player1! Enter your name: ")
    player2name = input("Hi player2! Enter your name: ")
    return player1name, player2name


playing_right_now_tuple = get_player_names()  # This line calls the get_player_names() function and assigns the returned tuple of player names to the variable playing_right_now_tuple.

print(f"{playing_right_now_tuple[0]} and {playing_right_now_tuple[1]} are currently playing dice")


def dice_roll():  # This function simulates rolling a dice by generating a random number between 1 and 6 (inclusive) and returns the result.
    diceRoll = random.randint(1, 6)
    return diceRoll


def play():  # This function represents the main gameplay logic.
    player1 = 0  # It initializes variables for player scores, wins, and rounds.
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 0

    while rounds != 3:  # It then enters a loop to play 3 rounds.
        rounds = rounds + 1
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print(f"{playing_right_now_tuple[0]} " + str(player1))
        print(f"{playing_right_now_tuple[1]} " + str(player2))

        if player1 == player2:  # Rolls dice for players, compares the results and keeps track of number of wins.
            print("It's a draw!")
        elif player1 > player2:
            player1wins = player1wins + 1
            print(f"{playing_right_now_tuple[0]} wins 🏆!")
        else:
            player2wins = player2wins + 1
            print(f"{playing_right_now_tuple[1]} wins 🏆!")

    if player1wins == player2wins:  # Finally, it prints the final result based on the number of wins.
        print("Final score is a draw")
    elif player1wins > player2wins:
        print(f"{playing_right_now_tuple[0]} wins overall 🏆🏆🏆! Rounds won: " + str(player1wins))
    else:
        print(f"{playing_right_now_tuple[1]} wins overall 🏆🏆🏆! Rounds won: " + str(player2wins))


play()  # This line calls the play() function to start the game.
continue_playing = "y"
while continue_playing == "y":
    continue_playing = input("want to play again(y/n):")
    if continue_playing == "y":
        print("Go for it!")
        play()
    else:
        print("Thank you for playing!")

import random  # This line imports the random module, which allows generating random numbers.


def get_player_names():  # to customise the game with a set of values(here the players' names), we've used a tuple
    player1name = input("Hi player1! Enter your name: ")
    player2name = input("Hi player2! Enter your name: ")
    return player1name, player2name


playing_right_now_tuple = get_player_names()  # This line calls the get_player_names() function and assigns the returned tuple of player names to the variable playing_right_now_tuple.

print(f"{playing_right_now_tuple[0]} and {playing_right_now_tuple[1]} are currently playing dice")


def dice_roll():  # This function simulates rolling a dice by generating a random number between 1 and 6 (inclusive) and returns the result.
    diceRoll = random.randint(1, 6)
    return diceRoll


def play():  # This function represents the main gameplay logic.
    player1 = 0  # It initializes variables for player scores, wins, and rounds.
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 0

    while rounds != 3:  # It then enters a loop to play 3 rounds.
        rounds = rounds + 1
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print(f"{playing_right_now_tuple[0]} " + str(player1))
        print(f"{playing_right_now_tuple[1]} " + str(player2))

        if player1 == player2:  # Rolls dice for players, compares the results and keeps track of number of wins.
            print("It's a draw!")
        elif player1 > player2:
            player1wins = player1wins + 1
            print(f"{playing_right_now_tuple[0]} wins 🏆!")
        else:
            player2wins = player2wins + 1
            print(f"{playing_right_now_tuple[1]} wins 🏆!")

    if player1wins == player2wins:  # Finally, it prints the final result based on the number of wins.
        print("Final score is a draw")
    elif player1wins > player2wins:
        print(f"{playing_right_now_tuple[0]} wins overall 🏆🏆🏆! Rounds won: " + str(player1wins))
    else:
        print(f"{playing_right_now_tuple[1]} wins overall 🏆🏆🏆! Rounds won: " + str(player2wins))


play()  # This line calls the play() function to start the game.
continue_playing = "y"
while continue_playing == "y":
    continue_playing = input("want to play again(y/n):")
    if continue_playing == "y":
        print("Go for it!")
        play()
    else:
        print("Thank you for playing!")

