#You are playing an antique RPG game.
#You are asked for your age. returns a message depending on whether player is over 18.
#You are asked if you want to read an introduction to the game.
#If you choose yes, it will print out a brief introduction.
#
#
def ansprocess(answer):
    return bool(answer)
def legalage(legal):
    if ansprocess(legal):
        print "Warning:\nYou will be psychologically scarred if you continue."
def introduction(intro):
    if ansprocess(intro):
        print "This is a simple game where you are going to play a few ridiculously childish minigames."
def mazeloop(maze):
    if ansprocess(maze):
        print "You wander the maze for hours, eventually stumbling onto a teleporter that returns you to the start of the maze."
        maze = raw_input("Do you wish to attempt the maze again? ")
        mazeloop(maze)
    else:
        print "You decide to go around the maze instead of going through it."
def main():
    #Input
    print "In this game, if you wish to say no to a question, do not type anything and press enter."
    legal = raw_input("Greetings, Traveler.\nAre you under the age of 18? ")
    legalage(legal)
    intro = raw_input("Do you wish to read an introduction to the game? ")
    introduction(intro)
    print "You encounter a large maze. There seems to be some reward if you pass through it."
    maze = raw_input("Do you wish to attempt the maze or not? ")
    mazeloop(maze)
    #Processing
    
    #Output
main()
