# Kayla Jones
# Project 2
import math
import random


# receives the user's character name
def get_name():
    character_name = input("Welcome, adventurer! What's your name? ")
    return character_name


# calculates character stats by rolling four six sided dice
def sum_of_four_six_sided_dice_with_lowest_dropped():
    # initializes lowest_value variable before generating random numbers
    # set to 7 since we're working with a six sided die
    lowest_value = 7

    # generates four random numbers from a six sided die
    # supposed to replicate the act of throwing the die four times
    # also checks if the value is lower than the lowest value and
    # updates the lowest value as the other values are being generated
    four_six_sided_die_first_value = random.randint(1,6)
    if four_six_sided_die_first_value < lowest_value:
        lowest_value = four_six_sided_die_first_value

    four_six_sided_die_second_value = random.randint(1, 6)
    if four_six_sided_die_second_value < lowest_value:
        lowest_value = four_six_sided_die_second_value

    four_six_sided_die_third_value = random.randint(1, 6)
    if four_six_sided_die_third_value < lowest_value:
        lowest_value = four_six_sided_die_third_value

    four_six_sided_die_fourth_value = random.randint(1, 6)
    if four_six_sided_die_fourth_value < lowest_value:
        lowest_value = four_six_sided_die_fourth_value

    # finds the sum of the 3 largest numbers
    sum_of_largest_three = (four_six_sided_die_first_value+four_six_sided_die_second_value
                            +four_six_sided_die_third_value+four_six_sided_die_fourth_value)-lowest_value
    return sum_of_largest_three

# getter functions to find player's strength, dexterity, constitution,
# intelligence, wisdom, and charisma stats
def get_strength():
    strength = sum_of_four_six_sided_dice_with_lowest_dropped()
    return strength

def get_dexterity():
    dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
    return dexterity

def get_constitution():
    constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
    return constitution

def get_intelligence():
    intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
    return intelligence

def get_wisdom():
    wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
    return wisdom

def get_charisma():
    charisma = sum_of_four_six_sided_dice_with_lowest_dropped()
    return charisma

# getter functions that calculate ability modifiers for each character stat
# rounds down if there is a decimal result
def get_strength_ability_modifier():
    strength = get_strength()
    strength_ability_modifier = math.floor((strength-10)/2)
    return strength_ability_modifier

def get_dexterity_ability_modifier():
    dexterity = get_dexterity()
    dexterity_ability_modifier = math.floor((dexterity-10)/2)
    return dexterity_ability_modifier

def get_constitution_ability_modifier():
    constitution = get_constitution()
    constitution_ability_modifier = math.floor((constitution-10)/2)
    return constitution_ability_modifier

def get_intelligence_ability_modifier():
    intelligence = get_intelligence()
    intelligence_ability_modifier = math.floor((intelligence-10)/2)
    return intelligence_ability_modifier

def get_wisdom_ability_modifier():
    wisdom = get_wisdom()
    wisdom_ability_modifier = math.floor((wisdom-10)/2)
    return wisdom_ability_modifier

def get_charisma_ability_modifier():
    charisma = get_charisma()
    charisma_ability_modifier = math.floor((charisma-10)/2)
    return charisma_ability_modifier

# returns a random treasure from the list of treasures
def get_treasure():
    treasures = ['gems', 'gold', 'jade figurine', 'silver']
    return random.choice(treasures)

# starts game
def menu():
    # displays character name
    character_name = get_name()
    print("Welcome, " + character_name + "!")

    # gets character stat ability modifiers
    strength_ability_modifier = get_strength_ability_modifier()
    dexterity_ability_modifier = get_dexterity_ability_modifier()
    constitution_ability_modifier = get_constitution_ability_modifier()
    intelligence_ability_modifier = get_intelligence_ability_modifier()
    wisdom_ability_modifier = get_wisdom_ability_modifier()
    charisma_ability_modifier = get_charisma_ability_modifier()

    number_of_choices_made = 0
    while number_of_choices_made < 4: # player can run the game 4 times
        print("Let's start a new adventure! What will do you?")
        choice = int(input(("1 - Attack\n2 - Negotiate\n3 - Search\n4 - Eat\n")))

        if choice == 1: # if player chooses attack
            print("You rolled a 20 sided die!")
            twenty_sided_die = random.randint(1, 20)
            print("You got a: " + str(twenty_sided_die) + "!")

            attack_total = 0
            if strength_ability_modifier > dexterity_ability_modifier:
                larger_attack_modifier = strength_ability_modifier
                attack_total = strength_ability_modifier + twenty_sided_die
                print("Your attack total is: ", attack_total)
            elif dexterity_ability_modifier > strength_ability_modifier:
                larger_attack_modifier = dexterity_ability_modifier
                attack_total = dexterity_ability_modifier + twenty_sided_die
                print("Your attack total is:", attack_total)

            if attack_total >= 12:
                print("You hit!")
                six_sided_die = random.randint(1, 6)
                total_damage = larger_attack_modifier + six_sided_die
                print("Total damage:", total_damage)
            else:
                print("You missed!\n")

        elif choice == 2: # if player chooses negotiate
            print("You rolled a 20 sided die!")
            twenty_sided_die = random.randint(1, 20)
            print("You got a: " + str(twenty_sided_die) + "!")
            negotiation_total = charisma_ability_modifier + twenty_sided_die
            print("Your negotiation total is:", negotiation_total)

            if negotiation_total >= 15:
                print("You successfully negotiated a truce!\n")
            else:
                print("Your negotiation was not a success.\n")

        elif choice == 3: # if player chooses search
            print("You rolled a 20 sided die!")
            twenty_sided_die = random.randint(1, 20)
            print("You got a: " + str(twenty_sided_die) + "!")

            if intelligence_ability_modifier > wisdom_ability_modifier:
                larger_search_modifier = intelligence_ability_modifier
                search_total = larger_search_modifier + twenty_sided_die
                print("Your search total is:", search_total)
            elif wisdom_ability_modifier > intelligence_ability_modifier:
                larger_search_modifier = wisdom_ability_modifier
                search_total = larger_search_modifier + twenty_sided_die
                print("Your search total is:", search_total)

            if search_total >= 12:
                print("You found treasure! Let's see what you found!\n")
                print("You found:", get_treasure())
            else:
                print("You found nothing.\n")

        elif choice == 4: # if player chooses eat
            print("Your food was rancid! Ew!")
            print("You rolled a 20 sided die!")
            twenty_sided_die = random.randint(1, 20)
            print("You got a: " + str(twenty_sided_die) + "!")
            eat_total = constitution_ability_modifier + twenty_sided_die

            if eat_total >= 10:
                print("Luckily, you were able to handle the rancid food without getting sick.\n")
            else:
                print("You got sick and need to stay in bed for a while.\n")

        number_of_choices_made += 1

    print("Thanks for playing, " + character_name + "!")

menu()
