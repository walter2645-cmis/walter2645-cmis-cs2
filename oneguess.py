import random
def difference(userguess, randnum):
    return abs(userguess - randnum)
def compare(userguess, randnum):
    if randnum == userguess:
        return "correct"
    elif randnum > userguess:
        return "under"
    elif randnum < userguess:
        return "over"
def output1(randnum, userguess):
    out = """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""".format(randnum, userguess)
    return out
def output2(randnum, userguess, differenceres):
    out = """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(randnum, userguess, differenceres)
    return out
def output3(randnum, userguess, differenceres):
    out = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(randnum, userguess, differenceres)
    return out
def main():
    #Input
    min_num = int(raw_input("What is the minimum number? "))
    max_num = int(raw_input("What is the maximum number? "))
    userguess = int(raw_input("I'm thinking of a number from " + str(min_num) + " to " + str(max_num) + ".\nWhat do you think it is?: "))

    #Processing
    randnum = random.randint(min_num, max_num)
    compareres = compare(userguess, randnum)
    differenceres = difference(userguess, randnum)
    if compareres == "correct":
        outp = output1(randnum, userguess)
    elif compareres == "over":
        outp = output2(randnum, userguess, differenceres)
    elif compareres == "under":
        outp = output3(randnum, userguess, differenceres)
    #Output
    print outp
main()
