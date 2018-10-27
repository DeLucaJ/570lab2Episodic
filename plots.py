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
	{"name": "Artificer", "method": "mechanical contraptions", "gear": "invention"},
	{"name": "Barbarian", "method": "incredible strength", "gear": "greataxe"}, 
	{"name": "Bard", "method": "irresistible charm", "gear": "instrument"}, 
	{"name": "Cleric", "method": "divine power", "gear": "holy symbol"}, 
	{"name": "Druid", "method": "power of nature", "gear": "oak staff"}, 
	{"name": "Fighter", "method": "blunt force", "gear": "hammer"},
	{"name": "Monk", "method": "skillful martial arts", "gear": "martial arts"}, 
	{"name": "Mystic", "method": "psychic abilities", "gear": "mind"},
	{"name": "Paladin", "method": "a divine smite", "gear": "holy sword"}, 
	{"name": "Ranger", "method": "unmatched survival skills", "gear": "bow"}, 
	{"name": "Rogue", "method": "amazing agility", "gear": "dagger"}, 
	{"name": "Sorcerer", "method": "innate magic", "gear": "arcane orb"}, 
	{"name": "Warlock", "method": "dark secrets", "gear": "wand"}, 
	{"name": "Wizard", "method": "unfathomable intellect", "gear": "crystal staff"}
]

# A list of dictionaries?
villains = [
	{"name": "Dragon", "minions": "kobolds", "lair": "secret treasure room"},
	{"name": "Lich", "minions": "necromancers", "lair": "hidden extraplanar doom"},
	{"name": "Mind Flayer", "minions": "intellect devourers", "lair": "laboratory"},
	{"name": "Beholder", "minions": "eyeball monsters", "lair": "heavily booby-trapped chamber"},
	{"name": "Emperyan", "minions": "gladiators", "lair": "coliseum"},
	{"name": "Tarrasque", "minions": "cultists", "lair": "awakening chamber"},
	{"name": "Necromancer", "minions": "skeletons", "lair": "graveyard"},
	{"name": "Archmage", "minions": "wizards", "lair": "ritual chamber"},
	{"name": "Vampire", "minions": "bats", "lair": "invisible mansion"},
	{"name": "Kraken", "minions": "merfolk", "lair": "alternate ocean plane"},
	{"name": "Archdevil", "minions": "imps", "lair": "blazing throne room"},
	{"name": "Archdemon", "minions": "quasits", "lair": "maddening chaos-scape"},
	{"name": "Corrupt Angel", "minions": "ghosts", "lair": "a harrowing realm"},
	{"name": "Leviathan", "minions": "air elementals", "lair": "the sky"},
	{"name": "Million Goblins", "minions": "goblins", "lair": "hidden goblin cave complex"}
]

treasures = [
	{"name": "the shoe of a thousand truths", "property": "It stinks of knowledge"},
	{"name": "the holy sword, Excalibur", "property": "It shines with divine power"},
	{"name": "the unholy sword, Rubilacxe", "property": "It seems to suck in the light around it"},
	{"name": "the abnormally normal sword, Sword", "property": "It doesn't seem special"},
	{"name": "a tome of lost magical secrets", "property": "It contains spells lost to time"},
	{"name": "a sphere of annihilation", "property": "All that passes through it is destroyed"},
	{"name": "a talisman of pure good", "property": "It radiates with the power of justice"},
	{"name": "a talisman of ultimate evil", "property": "It emanates a dark aura"},
	{"name": "the ultimate shield, Aegis", "property": "It cannot be pierced"},
	{"name": "the deck of many things", "property": "Draw at your own risk"},
	{"name": "the book of economancy, The Economicon", "property": "It radiates capitalism"},
	{"name": "the book of death, The Necronomicon", "property": "It radiates death"}
]

escape_route = [
	"through a secret passage",
	"by teleporting to another plane"
	"by transferring their soul to another body",
	"turning into mist and flying away",
	"using a henchmen as a meat-shield"
]

locations = [
	{"name": "hidden tower", "guardian": "an arcane golem"},
	{"name": "sprawling underground mega-dungeon", "guardian": "an army of giant rats"},
	{"name": "mysterious forest", "guardian": "a mischievous fog spirit"},
	{"name": "ancient lost city", "guardian": "a 100 foot tall ancient colossus"},
	{"name": "floating fortress", "guardian": "a giant eagle with a 50 foot wingspan"},
	{"name": "underwater temple", "guardian": "a pod of sentient killer whales"},
	{"name": "castle on the peak of the tallest mountain", "guardian": "an army of angry giants"},
]

#can currently use person1, person2, gear1, method1, and minions
setbacks = [
	"the {person1} had their {gear1} taken by {minions}, and the party got sidetracked retrieving it",
	"the path to their goal was destroyed so {person1} used their {method1} to find another way around",
	"the {person1} was killed in action, and the party had to continue without them",
	"the {person1} betrayed the party, killing the {person2} with their {gear1}, but eventually fell to {person3}",
	"the party found their goal, but it was actually an illusion to hide the real goal",
	"the party got swarmed by {minions} and needed to escape"
]

# Can currently use attributes guard and minions
challenges = [
	"solve the riddle of the {guard}",
	"defeat {guard}",
	"perform the secret ritual of passage",
	"hide from {minions}",
	"break the magic seal",
]

resolutions = [
	"Despite The Party's efforts, The {villain} escaped {via}",
	"After a grueling battle, The Part defeated The {villain}",
	"After defeating The {villain}, The Party discoverd the true villain was The {villain2} all along",
	"The Party could not defeat The {villain}. However, they managed to narrowly escape.",
	"The fight was long and difficult, but when The Party finally got the upper hand they discovered the villain was only an illusion.",
	"The Party decided to retreat when The {villain}'s ally, The {villain2} appeared with an army of {minions2}."
]

# Grabs and removes a random class from the list.
def grab_attribute(l):

	item = random.sample(l, 1)
	l.remove(item[0])
	return item[0]

# Dungeon location
def location(location, villain):

	return "The Party arrived at the {place}.".format(place = location.get("name"))

# Puzzle or Role-playing Challenge
def challenge(location, villain):

	person = grab_attribute(classes)

	return "{who}{what}.".format(
		who = "The {name} had to use their {method} to ".format(
			name = person.get("name"), 
			method = random.sample([person.get("method"), person.get("gear")], 1)[0]
		),
		what = grab_attribute(challenges).format(
			guard = location.get("guardian"),
			minions = villain.get("minions"),
		)
	)

# Trick or Setback
def trick(location, villain):

	person = grab_attribute(classes)
	victim = grab_attribute(classes)
	savior = grab_attribute(classes)

	return grab_attribute(setbacks).format(
		person1 = person.get("name"),
		method1 = person.get("method"),
		gear1 = person.get("gear"),
		person2 = victim.get("name"),
		minions = villain.get("minions"),
		person3 = savior.get("name")
	)

# The Big Climax / Boss Fight
def climax(location, villain):

	transitions = [
		"Finally,",
		"After a year of delving,",
		"Before they knew it,",
		"After a long night of delving,",
		"Through some sort of magical shenanigans,"
	]

	return "{transition} The Party reached their goal, only to face The {boss} in its {lair}".format(
		transition = grab_attribute(transitions),
		boss = villain.get("name"),
		lair = villain.get("lair")
	)

# Reward or Resolution
def resolution(location, villain):

	route = grab_attribute(escape_route)
	end = grab_attribute(resolutions)
	villain2 = grab_attribute(villains)

	return end.format(
		villain = villain.get("name"),
		via = route,
		villain2 = villain2.get("name"),
		minions2 = villain2.get("minions")
	)

def treasure(location, villain):

	reward = grab_attribute(treasures)

	return "As reward for their efforts, The Party received the {artifact}. {prop}.".format(
		artifact = reward.get("name"),
		prop = reward.get("property")
	)

# Main Function
def main():
	the_villan = grab_attribute(villains)
	the_location = grab_attribute(locations)

	plot = "{0}\nOnce inside, {1}\nLater on during their delve {2}\n{3}\n{4}\n{5}".format(
		location(the_location, the_villan),
		challenge(the_location, the_villan), 
		trick(the_location, the_villan),
		climax(the_location, the_villan),
		resolution(the_location, the_villan),
		treasure(the_location, the_villan)
	)
	print(plot)

if __name__ == '__main__':
	main()