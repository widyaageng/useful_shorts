"""
To be imported and used
to clear the screen in python terminal
with clscreen()
"""
import os

def clscreen():
	os.system('cls' if os.name == 'nt' else 'clear')