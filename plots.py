'''
Title:		Five Room Dungeon Adventure Generator
Author:		Joseph DeLuca
Assignment:	CSC 570 | Lab 2 - Episodic
Professor:	Dr. Foaad Khosmood
Date:		October 2018
'''
# The terminals
boss = ["bossA", "bossB", "bossC"],
condition = ["conditionA", "conditionB", "conditionC"],
enemy = ["enemyA", "enemyB", "enemyC"],
environment = ["environmentA", "environmentB", "environmentC"],
location = ["locationA", "locationB", "locationC"]
npc = ["npcA", "npcB", "npcC"],
physicalBarrier = ["physicalBarrierA", "physicalBarrierB", "physicalBarrierC"],
puzzle = ["puzzleA", "puzzleB", "puzzleC"],
setback = ["setbackA", "setbackB", "setbackC"],
trap = ["trapA", "trapB", "trapC"]

# Dungeon Entrance with a guardian
def entrance():

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
		entrance(),
		challenge(), 
		trick(),
		climax(),
		resolution()
	)

# Main Function
def main():

	plot = episode()
	print(plot)

if __name__ == '__main__':
	main()