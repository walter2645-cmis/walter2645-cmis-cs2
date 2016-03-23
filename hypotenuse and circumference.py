import math
def hypotenuse(x, y):
    return math.sqrt((x ** 2) + (y ** 2))
def circumference(a):
    return a ** 2 * math.pi
def output(name, triangleside1, triangleside2, hypresult, circleradius, circumferenceresult):
    out = """
Greetings, {}.
Did you know:
The length of the hypotenuse of a right triangle with side lengths {} and {} is {}
The circumference of a circle with radius {} is {}.
""".format(name, triangleside1, triangleside2, hypresult, circleradius, circumferenceresult)
    return out
def main():
    #Input Section
    name = raw_input("What is your name?\n")
    triangleside1 = int(raw_input("Type a number\n"))
    triangleside2 = int(raw_input("Type another number\n"))
    circleradius = int(raw_input("Type another number\n"))

    #Processings
    hypresult = hypotenuse(triangleside1, triangleside2)
    circumferenceresult = circumference(circleradius)

    #Output Section
    res = output(name, triangleside1, triangleside2, hypresult, circleradius, circumferenceresult)
    print res
main()
