#!/usr/bin/env python3

charname = input("Which character do you want to know about (Flash, Batman or Superman)?")

statname = input("What statistic do you want to know about? (Speed, Intelligence, Strength)?")

switch = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}

statvalue = switch.get(charname).get(statname)
print(charname + "'s " + statname + " is " + statvalue)

