def compguess():
    judgement = raw_input("too (h)igh, too (l)ow, or (c)orrect: ")
    if judgement == "c":
        return "I'm awesome!"
    elif judgement == "h":
        compguess()
    elif judgement == "l":
        compguess()
