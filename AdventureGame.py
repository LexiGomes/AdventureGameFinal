import time
import random
villain = ['dragon', 'troll', 'bear', 'lion', 'dark magician']
villain_chosen = random.choice(villain)


def print_pause(message, seconds = 2):
    """
    Deze functie zorgt ervoor dat er telkens een korte stop
    is van 2 secondes elke keer een bericht op het 
    scherm verschijnt. Tegelijkertijd kan ik ook
    bepalen of ik bij bepaalde berichten de stop juist 
    langer of korter wil. 
    """
    print(message)
    time.sleep(seconds)


def play_again():
    """
    Deze functie vraagt aan de speler of ze opnieuw willen spelen. 
    Input:
        Opnieuw spelen?: speler moet ja of nee invoeren en dit kan 
        gebeuren met hoofdletters of met kleine letters.
    Behavior:
        Als de speler weer wilt spelen, begint het spel opnieuw.  
        Als de speler niet weer wilt spelen dan stop de game.  
        Als de speler geen geldig waarde invoert, dan blijft de functie
        vragen naar een geldig waarde. 
    """
    again = input("Would you like to play again? (yes/no)\n").lower()
    while True:
        if "yes" in again:
            print_pause("Excelent! Restarting the game...")
            play_game()
            break
        elif "no" in again:
            print_pause("Alright. Thank you for playing!")
            break
        else:
            again = input("Please enter a 'yes' or 'no'.\n")


def intro():
    """
    Deze functie is de introductie tot het spel. Dit krijgt de speler
    te zien wanneer het spel start. 
    """
    print_pause("You find yourself standing in an open field, filled"
                " with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain_chosen} is somewhere around "
                "here, and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.")
    print_pause("To your right as a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")


def house(items):
    """
    Functie die bepaalt wat voor opties de speler heeft 
    wanneer hij zich in het huis bevindt en hoe het spel 
    zich afloopt. 
    Input:
        items: speler heeft het schild en het zwaard (niet?)
    Behavior:
        Als de speler de items heeft dan wint hij/zij het spel.  
        Als de speler de items niet heeft wordt hem de keuze 
        gegeven om toch te vechten of om terug naar het veld te gaan. 
        Als de speler geen geldig waarde invoert, dan blijft de functie
        vragen naar een geldig waarde. 
    """
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {villain_chosen}.")
    print_pause(f"Eep! This is a {villain_chosen}'s house!")
    decision = input("Would you like to (1) fight or (2) run away?\n")
    while True:
        if decision == "1":
            if "sword" in items:
                print_pause(f"As the {villain_chosen} moves to attack, you "
                            "unsheath your new sword and you ready "
                            "your shield.")
                print_pause("The sword of Ogoroth and Shield of "
                            "Westoros shine brightly in your "
                            "possession as you brace yourself for the "
                            f"attack.\nBut the {villain_chosen} takes "
                            "one look at you shiny new toys and " 
                            "runs away!", 3)
                print_pause("You have rid the town of the dragon. "
                            "You are victorious!")
                play_again()
                break
            else:
                print_pause(f"The {villain_chosen} attacks you! You feel "
                            "a bit under-prepared for this, what "
                            "with only having a tiny dagger.", 2.5)
                print_pause(f"You do your best...but your dagger is no "
                            f"match for the {villain_chosen}.")
                print_pause("You have been defeated.")
                play_again()
                break
        elif decision == "2":
            print_pause("You run as fast as you can back into the field.")
            print_pause("You trip over a piece of wood on your way "
                        f"out, the {villain_chosen} almost grabs you foot.")
            print_pause("You stand up and run as fast as you can "
                        "back into the field safely. Luckily, "
                        "you don't seem to have been followed.", 2.5)
            field(items)
            break
        else:
            decision = input("Would you like to (1) fight or (2) run away?\n")


def cave(items):
    """
    Deze functie is alleen bedoeld om de items te pakken om verder met 
    het verhaal te kunnen gaan. 
    Aan het eind wordt het zwaard en het schild aan de list 
    'items' toegevoegd.
    """
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be a very small cave and your "
                "eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth "
                "and the unbeatable Shield of Westoros.")
    print_pause("You discard your silly old dagger and take "
                "the sword with you.\nYou walk back out "
                "to the field.", 3)
    items.append("sword")
    field(items)


def field(items):
    """
    Function decides what options the player has 
    when he is in the field. 
    Input:
        items: speler heeft het schild en het zwaard (niet?)
        Speler kiest op het veld of hij naar het huis wilt of naar de grot. 
    Behavior:
        Als de speler een keuze maakt dan worden de overeenkomende 
        functies geroepen. 
        Als de speler geen geldig waarde invoert, dan blijft de functie
        vragen naar een geldig waarde. 
    """  
    print_pause("What would you like to do?")
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "Please enter 1 or 2.\n")
    while True:
        if choice == "1":
            house(items)
            break
        elif choice == "2":
            cave(items)
            break
        else:
            choice = input("Please, enter '1' or '2'.\n")


def play_game():
    """
    Deze functie brengt de game samen door de items list te 
    definiëren en uiteindelijk de intro functie en de field 
    functie te roepen. 
    """
    items = []
    intro()
    field(items)


if __name__ == '__main__':
    """
    Ik heb dit gedaan zodat mijn game alleen kan worden 
    geroepen als je code wordt uitgevoerd als een script. 
    Anders zou mijn hele code al uitgevoerd worden als 
    het .py bestand geïmporteerd word.
    """
    play_game()
