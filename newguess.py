import random
def rounds(roundnum, myscore, compscore):
    if roundnum == 0:
        return "You got " + str(myscore) + " rounds correct. I got " + str(compscore) + " rounds correct."
    else:
        print "Starting round " + str(roundnum)
        myscore += guess(random.randint(1, 100), 5)
        compscore += compguess(1, 100, 5)
        return rounds(roundnum - 1, myscore, compscore)
def guess(randnum, attempts):
    inp = int(raw_input("Guess a number: "))
    if inp == randnum:
        print "That's correct!\n"
        return 1
    elif attempts == 1:
        print "The answer was " + str(randnum) + ". You must not be very good at this game.\n"
        return 0
    elif inp > randnum:
        print "Thats too high."
        return guess(randnum, attempts - 1)
    elif inp < randnum:
        print "Thats too low."
        return guess(randnum, attempts - 1)
def compguess(bot, top, attempts):
    if attempts == 1:
        theguess = random.randint(bot, top)
    else:
        theguess = (top - bot) / 2 + bot
    print "I guess " + str(theguess) + "."
    judgement = raw_input("too (h)igh, too (l)ow, or (c)orrect: ")
    if judgement == "c":
        print "I'm awesome!"
        return 1
    elif attempts == 1:
        print "I must not be very good at this game."
        return 0
    elif judgement == "h":
        top = theguess
        return compguess(bot, top, attempts - 1)
    elif judgement == "l":
        bot = theguess
        return compguess(bot, top, attempts - 1)
def main():
    res = rounds(1, 0, 0)
    print res
main()
