import math
def circlecircumference():
    radius = int(raw_input("How many units long is the radius?\n"))
    unit = raw_input("What is the unit of measurment?\n")
    return "The measurement of the circumference of the circle is " + str(2 * math.pi * radius) + unit + "(s)."
def hypotenuseofrighttriangle():
    x = int(raw_input("How many units long is 1 side of the right triangle?\n"))
    y = int(raw_input("How many units long is the other side of the right triangle?\n"))
    unit = raw_input("What is the unit of measurement?\n")
    return "The hypotenuse of the right triangle is " + str(math.sqrt((x * x) + (y * y))) + unit + "(s) long."
print hypotenuseofrighttriangle()
