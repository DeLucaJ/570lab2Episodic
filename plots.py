'''
Title:		Five Room Dungeon Adventure Generator
Author:		Joseph DeLuca
Assignment:	CSC 570 | Lab 2 - Episodic
Professor:	Dr. Foaad Khosmood
Date:		October 2018
'''

import random

# If a class has been used, do not use again
# A list of dictionaries
classes = [
	{"name": "Artificer", "method": "mechanical contraptions"},
	{"name": "Barbarian", "method": "incredible strength"}, 
	{"name": "Bard", "method": "irresistible charm"}, 
	{"name": "Cleric", "method": "divine power"}, 
	{"name": "Druid", "method": "the power of nature"}, 
	{"name": "Fighter", "method": "blunt force"},
	{"name": "Monk", "method": "skillful martial arts"}, 
	{"name": "Mystic", "method": "psychic abilities"},
	{"name": "Paladin", "method": "a divine smite"}, 
	{"name": "Ranger", "method": "unmatched survival skills"}, 
	{"name": "Rogue", "method": "amazing agility"}, 
	{"name": "Sorcerer", "method": "innate magic"}, 
	{"name": "Warlock", "method": "dark secrets"}, 
	{"name": "Wizard", "method": "unfathomable intellect"}
]

# A list of dictionaries?
villain = [
	"Dragon",
	"Lich",
	"Mind Flayer",
	"Beholder",
	"Emperyan",
	"Tarrasque",
	"Necromancer",
	"Archmage",
	"Vampire",
	"Kraken",
	"Archdevil",
	"Archdemon",
	"Corrupt Angel",
	"Leviathan",
	"1,000,000 Goblins"
]

treasure = [
	"the shoe of a thousand truths",
	"the holy sword, Excalibur",
	"the unholy sword, Rubilacxe",
	"the abnormally normal sword, Sword"
	"a tome of lost magical secrets",
	"a sphere of annihilation",
	"a talisman of pure good",
	"a talisman of ultimate evil",
	"the ultimate shield, Aegis",
	"the deck of many things",
	"the book of economancy, The Economicon",
	"the book of death, The Necronomicon"
]

escape_route = [
	"through a secret passage",
	"by teleporting to another plane"
	"by transferring their soul to another body",
	"turning into mist and flying away",
	"using a henchmen as a meat-shield"
]

# should probably have attributes
locations = [
	"a hidden tower",
	"a sprawling underground mega-dungeon",
	"a mysterious forest",
	"an ancient lost city",
	"a floating fortress",
	"an underwater temple",
	"a castle at the peak of the tallest mountain",
]

setbacks = [
	"The {Class} had their {Gear} stolen, and the party got sidetracked retrieving it",
	"The path to their goal was destroyed so the had to find another way around",
	"The {Class} was killed in action, and the party had to continue without them",
	"The {Class} betrayed the party, killing the {Class}, but eventually falling",
	"The party found their goal, but it was actually an illusion to hide the real goal",
	"The party got swarmed by {Minions} and needed to escape"
]

# Grabs and removes a random class from the list.
def grab_attribute(l):

	item = random.sample(l, 1)
	l.remove(item[0])
	return item[0]

# Dungeon location
def location():

# Puzzle or Role-playing Challenge
def challenge():

# Trick or Setback
def trick():

# The Big Climax / Boss Fight
def climax():

# Reward or Resolution
def resolution():

# The Beginning of the Grammar 
def episode():

	return "{0} {1} {2} {3} {4}".format(
		location(),
		challenge(), 
		trick(),
		climax(),
		resolution()
	)

# Main Function
def main():

	#plot = episode()
	#print(plot)

if __name__ == '__main__':
	main()