import math
def heightdifference():
    Fheight = int(raw_input("How many centimeters tall is your father?\n"))
    height = int(raw_input("How many centimeters tall are you?\n"))
    return "The difference in your heights is " + str(Fheight - height) + " centimeters."
print heightdifference()
