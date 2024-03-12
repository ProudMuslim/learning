import sys
import random


def game_start():
    print(f"""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
        When I say:         That means:
        Pico                One digit is correct but in the wrong position.
        Fermi               One digit is correct and in the right position.
        Bagels              No digit is correct.
        """)
    while True:
        launch_prompt = input(
            "Would you like to begin or would you like to leave ( 'P' for play/ 'L' for leave ): ").lower()
        if launch_prompt == "l":
            sys.exit()
        elif launch_prompt == "p":
            main()
            break
        else:
            continue


def check_if_bagels(pc, player):
    if set(player) & set(pc):
        return
    else:
        print("Bagels")


def check_if_pico_fermi(pc, player):
    for i, k in enumerate(player):
        if k in pc:
            if player[i] != pc[i]:
                print("pico")
            else:
                print("fermi")
    if pc in player:
        print("You GUESSED IT !")
        return True


def main():
    pc_guess = random.randint(100, 999)
    str_pc_guess = str(pc_guess)

    print(f"""I thought of a number!!!
You have 10 guesses to find it """)
    i = 1
    print(pc_guess)
    for _ in range(10):
        player_guess = input(f"Guess #{i}: ")
        check_if_bagels(str_pc_guess, player_guess)
        if check_if_pico_fermi(str_pc_guess, player_guess):
            break

        i += 1


game_start()
