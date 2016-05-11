def compguess(bot, top, attempts):
    theguess = (top - bot) / 2 + bot
    print "I guess " + str(theguess) + "."
    judgement = raw_input("too (h)igh, too (l)ow, or (c)orrect: ")
    if judgement == "c":
        return "I'm awesome!"
    elif attempts == 1:
        return "I must not be very good at this game."
    elif judgement == "h":
        top = theguess
        return compguess(bot, top, attempts - 1)
    elif judgement == "l":
        bot = theguess
        return compguess(bot, top, attempts - 1)
def main():
    cres = compguess(1, 100, 5)
    print cres
main()
