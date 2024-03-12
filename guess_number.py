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
        launch_prompt = input("Would you like to begin or would you like to leave ( 'P' for play/ 'L' for leave ): ").lower()
        if launch_prompt == "l":
            sys.exit()
        elif launch_prompt == "p":
            main()
            break
        else:
            continue


def check_if_bagels(pc,player):
    player_choice = []
    for i in player:
        player_choice.append(i)
    if set(player_choice) & set(pc):
        return
    else:
        print("Bagels")



def check_if_pico(pc,player):
    pc_list = list(pc)
    player_list = list(player)

    for i in range(len(player_list)):
        if player_list[i] in pc_list:
            if player_list[i] != pc_list[i]:
                print("pico")
                

def main():
    pc_guess = random.randint(100, 999)
    str_pc_guess = str(pc_guess)
    pc_guess_list = list(str_pc_guess)
    print(f"""I thought of a number!!!
You have 10 guesses to find it """)
    i = 1
    print(pc_guess)
    for _ in range(10):
        player_guess = input(f"Guess #{i}: ")
        check_if_bagels(pc_guess_list, player_guess)
        check_if_pico(pc_guess_list, player_guess)

        i += 1



game_start()
