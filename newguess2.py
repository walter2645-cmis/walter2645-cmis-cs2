def compguess(bot, top):
    theguess = (top - bot) / 2 + bot
    print "I guess " + str(theguess) + "."
    judgement = raw_input("too (h)igh, too (l)ow, or (c)orrect: ")
    if judgement == "c":
        return "I'm awesome!"
    elif judgement == "h":
        top = theguess
        return compguess(bot, top)
    elif judgement == "l":
        bot = theguess
        return compguess(bot, top)
compguess(1, 100)
def main():
    cres = compguess(1, 100)
