#You are playing an antique RPG game.
#You are asked for your age. returns a message depending on whether player is over 18.
#You are asked if you want to read an introduction to the game.
#If you choose yes, it will print out a brief introduction.
#You encounter a maze. You are given an option to attempt it or do not.
#If you attempt it, it will loop back to the start of the maze until you choose not to attempt it.
#
def ansprocess(answer):
    return bool(answer)
def printer(printorder):
    if printorder == 1:
        print
    elif printorder == 2:
        print
    elif printorder == 3:
        print
    elif printorder == 4:
        print
def mysterybox():
    if random.random == random.random:
        print "You are officially the luckiest person that ever existed. You are granted 3 wishes."
        #wishes function?
    else:
        print "The box instantly vanishes as you try to open it."
def legalage(legal):
    if ansprocess(legal):
        print "Warning:\nYou will be psychologically scarred if you continue."
def introduction(intro):
    if ansprocess(intro):
        print "This is a simple game where you are going to play a few ridiculously childish minigames."
def mazeloop(maze):
    if ansprocess(maze):
        print "You wander the maze for hours, eventually stumbling onto a teleporter that returns you to the start of the maze."
        maze = raw_input("\nDo you wish to attempt the maze again? ")
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
    print "\nA mysterious box with question marks carved all over its surface appears in front of you. There is a note on top of it. It says: \"This mystery box contains three wishes. However, there is only a 1 in a trillion chance it will not disappear when you open it.\""
    #Processing
    
    #Output
main()
