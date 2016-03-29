import random
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
        print "In this game, if you wish to say no to a question, do not type anything and press enter."
    elif printorder == 2:
        print "Warning:\nYou will be psychologically scarred if you continue."
    elif printorder == 3:
        print "This is a simple game where you are going to play a few ridiculously childish minigames."
    elif printorder == 4:
        print "You encounter a large maze. There seems to be some reward if you pass through it."
    elif printorder == 5:
        print "You wander the maze for hours, eventually stumbling onto a teleporter that returns you to the start of the maze."
    elif printorder == 6:
        print "You decide to go around the maze instead of going through it."
    elif printorder == 7:
        print "\nA mysterious box with question marks carved all over its surface appears in front of you. There is a note on top of it. It says: \"This mystery box contains three wishes. However, there is only a 1 in a billion chance it will not disappear when you open it.\""
    elif printorder == 8:
        print "You are officially the luckiest person that ever existed. You are granted 3 wishes. You cannot wish for more wishes, nor wish that these conditions are nullified."
    elif printorder == 9:
        print "The box instantly vanishes as you try to open it."
    elif printorder == 10:
        print "The box is replaced with another note, saying: \"Your wishes will be granted at the end of the game. Farewell.\""
    elif printorder == 11:
        print "You decide not to open the box and continue travelling."
    elif printorder == 12:
        print "You encounter a strange humanoid robot in your way. It tells you that you must answer a random math question in order to progress. If you answer wrong, the question may change."
    elif printorder == 13:
        print
    elif printorder == 14:
        print
    elif printorder == 15:
        print
    elif printorder == 16:
        print
    elif printorder == 17:
        print
    elif printorder == 18:
        print
def legalage(legal):
    if ansprocess(legal):
        printer(2)
def introduction(intro):
    if ansprocess(intro):
        printer(3)
def mazeloop(maze):
    if ansprocess(maze):
        printer(5)
        maze = raw_input("\nDo you wish to attempt the maze again? ")
        mazeloop(maze)
    else:
        printer(6)
def wishes(wish1, wish2, wish3):
    printer(10)
def mysterybox():
    if random.random() >= 0.9999999:
        printer(8)
        wish1 = raw_input("What is your first wish? ")
        wish2 = raw_input("What is your second wish? ")
        wish3 = raw_input("What is your third wish? ")
        wishes(wish1, wish2, wish3)
    else:
        printer(9)
def mysteryboxq(decision):
    if ansprocess(decision):
        mysterybox()
    else:
        printer(11)
def q1(answer):
    if answer == 7:
    else:
def q2(answer):
    if answer == 169:
    else:
def q3(answer):
    if answer == 11111:
    else:
def q4(answer):
    if answer == 9:
    else:
def q5(answer):
    if answer == 288:
    else:
def mathquestions(qnumber):
    if qnumber == 1:
        q1(int(raw_input("1+2*3 = ? ")))
    elif qnumber == 2:
        q2(int(raw_input("13*13 = ? ")))
    elif qnumber == 3:
        q3(int(raw_input("12345-1234 = ? ")))
    elif qnumber == 4:
        q4(int(raw_input("8-1*0+2/2 = ? ")))
    elif qnumber == 5:
        q5(int(raw_input("48/2(9+3) = ? ")))
def main():
    printer(1)
    legal = raw_input("Greetings, Traveler.\nAre you under the age of 18? ")
    legalage(legal)
    intro = raw_input("Do you wish to read an introduction to the game? ")
    introduction(intro)
    printer(4)
    maze = raw_input("Do you wish to attempt the maze or not? ")
    mazeloop(maze)
    printer(7)
    decision = raw_input("Do you wish to open it? ")
    mysteryboxq(decision)
    printer(12)
    randquestion = random.randint(1, 5)
    mathquestions(randquestion)
    #numbers >>random.randint next.
main()
