#!/usr/bin/env python3
import random

while True:
    ran_book = bool(random.getrandbits(1)) #Creating a random boolean value to display one of two books by the author
    print("\n\n################################################################## \n \n")
    print("Choose an author to display a summary of one of their works:")
    print("1. Kurt Vonnegut")
    print("2. Ray Bradberry")
    print("3. Orson Scott Card")
    print("4. George Orwell")
    print("Q. Quit")
    print("\n\n################################################################## \n \n")
    answer = input("Select an author (enter 1-4 or Q to quit):")
    if answer == '1':
        if ran_book == True:
            print("\u001b[31m\n\nPlayer Piano by Kurt Vonnegut - Depicts a dystopia of automation, describing the negative impact it can have on quality of life\u001b[37m")
        else:
            print("\u001b[31m\n\nSlaughterhouse Five by Kurt Vonnegut - About a man who travels between periods of his life unable to control what period he lands in\u001b[37m")
    elif answer == '2':
        if ran_book == True:
            print("\u001b[31m\n\nFahrenheit 451 by Ray Bradberry - Presents a future of american society where books are outlawed and firemen burn any that are foud\u001b[37m")
        else:
            print("\u001b[31m\n\nThe Martian Chronicles by Ray Bradberry - Chronicles the colonization of Mars by humans fleeing from a troubled earth.\u001b[37m")
    elif answer == '3':
        if ran_book == True:
            print("\u001b[31m\n\nEnder's Game by Orson Scott Card - This novel presents an imperiled humankind after two conflicts with the Formics, an insectoid alien species they dubbed the Buggers\u001b[37m")
        else:
            print("\u001b[31m\n\nEnder's Shadow by Orson Scott Card - A continuation of Ender's Game, showing the final battle against the Formics\u001b[37m")
    elif answer == '4':
        if ran_book == True:
            print("\u001b[31m\n\n1984 by George Orwell - Published in 1949 as a warning against totalitarianism. The chilling dystopia made a deep impression on readers, and his ideas entered the mainstream culture in a way acheived by very few books.\u001b[37m")
        else:
            print("\u001b[31m\n\nAnimal Farm by George Orwell - A story of a group of farm animals who rebel against their human farmer, hoping to create a society where all animals are equal\u001b[37m")
    elif answer == "q" or answer == "Q":
        print("\u001b[31m\nExiting\u001b[37m\n\n")
        break
    else:
        print("\n\nYou did not enter a valid input, try again")
