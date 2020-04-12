import random  # imports "random" used for dice rolls


# defines method "dice_roll"
def dice_roll():
    atk_wins = 0  # variable used to count defender army losses
    def_wins = 0  # variable used to count attacker army losses

    # variables for each of the potential six dice rolls
    # each dice roll is a random integer between 1 and 6
    atk_dice1 = random.randint(1, 6)
    atk_dice2 = random.randint(1, 6)
    atk_dice3 = random.randint(1, 6)
    def_dice1 = random.randint(1, 6)
    def_dice2 = random.randint(1, 6)
    def_dice3 = random.randint(1, 6)

    # creates list of attacker's dice rolls
    atk_dice = [atk_dice1, atk_dice2, atk_dice3]

    # amendments to number of attackers dice by amending number of elements in list
    atk_units = input("Enter total number of attacking units: ")
    if atk_units == "3":
        del atk_dice[2]
    elif atk_units == "2":
        del atk_dice[2]
        del atk_dice[1]
    elif atk_units == "1":
        print("Attacker doesn't have enough units to be able to attack.  Please try again.")
        dice_roll()  # starts again if attacker doesn't have enough units to attack

    # orders atk_dice list of attacker's dice rolls by highest to lowest
    atk_dice.sort()
    atk_dice.reverse()

    # creates list of defender's dice rolls
    def_dice = [def_dice1, def_dice2, def_dice3]

    # amendments to number of defenders dice by amending number of elements in list
    def_units = input("Enter total number of defending units: ")
    if def_units == "2":
        del def_dice[2]
    elif def_units == "1":
        del def_dice[2]
        del def_dice[1]
    elif def_units == "0":
        print("Defender is unable to defend.  Please try again.")
        dice_roll() # starts again if defender doesn't have enough units to defend

    # orders def_dice list of defender's dice rolls by highest to lowest
    def_dice.sort()
    def_dice.reverse()

    # comparison of attacker's and defender's dice rolls
    if len(atk_dice) > 0 and len(def_dice) > 0:
        if atk_dice[0] <= def_dice[0]:
            def_wins += 1
        else:
            atk_wins += 1

    if len(atk_dice) > 1 and len(def_dice) > 1:
        if atk_dice[1] <= def_dice[1]:
            def_wins += 1
        else:
            atk_wins += 1

    if len(atk_dice) > 2 and len(def_dice) > 2:
        if atk_dice[2] <= def_dice[2]:
            def_wins += 1
        else:
            atk_wins += 1

    # prints results of the dice rolls comparison
    print("\nAttacker rolls: " + str(atk_dice))
    print("Defender rolls: " + str(def_dice))
    print("\nAttacker wins " + str(atk_wins) + " dice rolls.\nDefender wins " + str(def_wins) + " dice rolls.")
    print("Attack loses " + str(def_wins) + " units.\nDefender loses " + str(atk_wins) + " units.")

    # asks the user if they want to play again or close the program
    user_input = input("\nPlay again? (Y/N)")
    user_input.lower()

    # program only closes if the user explicitly enters "n" or "no"
    if user_input != "n" and user_input != "no":
        print("\n")
        dice_roll()


dice_roll()
