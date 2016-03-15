import random
def compare(userguess, randnum):
    if randnum == userguess
        return correct
    elif randnum > userguess
        return under
    elif randnum < userguess
        return over
def determineoutput():
    if compareres = correct
        return out1
    elif compareres = under
        under = randnum - userguess
        return out2
def output1(randnum, userguess):
    out = """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""".format(randnum, userguess)
def output2(randnum, userguess, over):
    out = """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(randnum, userguess, over)
def output3(randnum, userguess, under):
    out = """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(randnum, userguess, under)
def main():
    #Input
    min_num = int(raw_input("What is the minimum number?"))
    max_num = int(raw_input("What is the maximum number?"))
    userguess = int(raw_input("I'm thinking of a number from " + str(min_num) + " to " + str(max_num) + ".\nWhat do you think it is?:"))

    #Processing
    randnum = random.randint(min_num, max_num)
    compareres = compare(userguess, randnum)
    #Output
    if 
