#!/usr/bin/env python3
import random

while True:
    print("\n\n################################################################## \n \n")
    print("Choose an author to display a summary of one of their works:")
    print("1. Kurt Vonnegut")
    print("2. Ray Bradberry")
    print("3. Orson Scott Card")
    print("4. George Orwell")
    print("Q. Quit")
    print("\n \n################################################################### \n \n")
    answer = input("Select an author (enter 1-4 or Q to quit):")
    if answer == '1':
        print("\u001b[31m\n\nPlayer Piano - Depicts a dystopia of automation, describing the negative impact it can have on quality of life\u001b[37m")
    elif answer == '2':
        print("\u001b[31m\n\nFahrenheit 451 - Presents a future of american society where books are outlawed and firemen burn any that are foud\u001b[37m")
    elif answer == '3':
        print("\u001b[31m\n\nEnder's Game - This novel presents an imperiled humankind after two conflicts with the Formics, an insectoid alien species they dubbed the Buggers\u001b[37m")
    elif answer == '4':
        print("\u001b[31m\n\n1984 - Published in 1949 as a warning against totalitarianism. The chilling dystopia made a deep impression on readers, and his ideas entered the mainstream culture in a way acheived by very few books.\u001b[37m")
    elif answer == "q" or answer == "Q":
        print("\u001b[31m\nExiting\u001b[37m\n\n")
        break
    else:
        print("\n\nYou did not enter a valid input, try again")
