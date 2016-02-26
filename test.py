def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
def text_comp(a, b):
    if a == b:
        return "Congratulations! You followed the instructions correctly!"
    else:
        return "sdfk"
def text_comp2():
    a = raw_input("Type anything:\n")
    b = raw_input("Type exactly what you typed just now again, please:\n")
    if a == b:
        return "Congratulations! You followed the instructions correctly!"
    else:
        return "sdfk"
def num_comp(c, d):
    if c == d:
        return "The numbers are equal."
    elif c > d:
        return "The first number is greater than the second number."
    elif c < d:
        return "The first number is less than the second number."
def num_comp2():
    a = float(raw_input("Type a number:\n"))
    b = float(raw_input("Type another number:\n"))
    if a == b:
        return "The numbers are equal."
    elif a > b:
        return "The first number is greater than the second number."
    elif a < b:
        return "The first number is less than the second number."
def output1():
    out = """
The results are...
"""
def output2():
def query():
    if e == "Yes"
        return output1
    elif e == "yes"
        return output1
    elif e == "No"
        return output2
    elif e == "no"
        return output2
def main():
    #Input Section
    name = raw_input("What is your name?\n")
    a = raw_input("Type anything.\n")
    b = raw_input("Type exactly what you typed just now again, please.\n")
    c = raw_input("Type a number.\n")
    d = raw_input("Type another number.\n")
    e = raw_input("Would you like to know something about what you just typed?(Yes/No)\n")

    #Processings
    f = text_comp(a, b)
    g = num_comp(c, d)

    #Output Section
