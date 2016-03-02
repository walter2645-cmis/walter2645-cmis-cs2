import math
def hypotenuse(x, y):
    return math.sqrt((x ** 2) + (y ** 2))
def circumference(a):
    return a ** 2 * math.pi
def output(name, x, y, z, a, b):
    out = """
Greetings, {}.
Did you know:
The length of the hypotenuse of a right triangle with side lengths {} and {} is {}
The circumference of a circle with radius {} is {}.
""".format(name, x, y, z, a, b)
    return out
def main():
    #Input Section
    name = raw_input("What is your name?\n")
    x = int(raw_input("Type a number\n"))
    y = int(raw_input("Type another number\n"))
    a = int(raw_input("Type another number\n"))

    #Processings
    z = hypotenuse(x, y)
    b = circumference(a)

    #Output Section
    res = output(name, x, y, z, a, b)
    print res
main()
