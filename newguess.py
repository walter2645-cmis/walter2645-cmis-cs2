import random
def rounds(roundnum, c):
    if roundnum == 0:
        return "You got " + str(c) + " rounds correct."
    else:
        print "Starting round " + str(roundnum)
        c += guess(random.randint(1, 100), 4)
        return rounds(roundnum - 1, c)
def guess(randnum, attempts):
    inp = int(raw_input("Guess a number: "))
    if inp == randnum:
        print "That's correct!\n"
        return 1
    elif attempts == 0:
        print "The answer was " + str(randnum) + ". You must not be very good at this game.\n"
        return 0
    elif inp > randnum:
        print "Thats too high."
        return guess(randnum, attempts - 1)
    elif inp < randnum:
        print "Thats too low."
        return guess(randnum, attempts - 1)
def main():
    res = rounds(1, 0)
    print res
main()
