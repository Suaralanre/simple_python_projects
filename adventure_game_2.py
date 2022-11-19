import time
import random

items = []


def print_pause(message_string, delay=0):
    print(message_string)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is'
                    'invalid. Try again!')


def intro_text():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause("Rumor has it that a " + enemies +
                " is somewhere around here, "
                "and has been terrifying the nearby village.", 2)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.", 2)


def field():
    reply = valid_input("Enter 1 to knock on"
                        " the door of the house \n"
                        "Enter 2 to peer into the cave\n", ["1", "2"])
    if reply == "2":
        cave()
    if reply == "1":
        house()
    house_choice()


def cave():
    if 'sword' in items:
        print_pause("\nYou peer cautiously into the cave.", 2)
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n", 2)
        field()
    else:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.", 2)
        print_pause("You walk back out to the field.", 2)
        items.append("sword")
        field()


def house():
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens"
                " and out steps a " + enemies + ".", 2)
    print_pause("Eep! This is the " + enemies + " house!", 2)
    print_pause("The " + enemies + " attacks you!", 2)


def fight_win():
    print_pause("As the " + enemies + " moves to attack,"
                " you unsheath your new sword.", 2)
    print_pause("The Sword of Ogoroth shines brightly in your"
                " hand as you brace yourself for the attack.", 2)
    print_pause("But the " + enemies + " takes one "
                "look at your shiny new toy and runs away!", 2)
    print_pause("You have rid the town of the " + enemies +
                " You are victorious!", 2)


def fight_lose():
    print_pause("You do your best...", 2)
    print_pause("but your dagger is no match for the " + enemies, 2)
    print_pause("You have been defeated!", 2)


def run_away():
    print_pause("You run back into the field. "
                "\nLuckily, you don't seem to have been "
                "followed.\n")
    field()


def house_choice():
    choice = valid_input("Would you like to fight (1) "
                         "or run away (2)?\n", ['1', '2'])

    if choice == "1":
        if "sword" in items:
            fight_win()
        else:
            fight_lose()

    if choice == "2":
        run_away()


def play_again():
    again = valid_input("\n\nWould you like to"
                        " play again? (y/n)\n", ["y", "n"])
    if again == "y":
        print_pause("\n\nExcellent! Restarting the game ...\n\n")
        play_game()
    if again == "n":
        print_pause("\n\n\nThanks for playing!"
                    " See you next time.\n\n\n")


def play_game():
    global enemies
    enemies = random.choice(["wicked fairie", "pirate", "dragon",
                             "troll", "gorgon"])
    intro_text()
    field()
    play_again()


if __name__ == "__main__":
    play_game()
