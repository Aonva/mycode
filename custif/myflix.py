#!/usr/bin/env python3

message = 'Your game with be starting soon, '

#
Avatar = input("Please select an Avatar. ")

#
if Avatar == "Elf":
    message = message + 'setting up elf profile.'
elif Avatar == "Warrior":
    message = message + 'setting up warrior profile.'
elif Avatar == "Rogue":
    message = message + 'setting up rogue profile.'
else:
    message = message + 'you did not provide input. Timed out!'
print(message)
