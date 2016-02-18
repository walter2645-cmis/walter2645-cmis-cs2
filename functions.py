import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return float(a) / b
def hours_from_seconds(a):
    return a / 3600
def circle_area(a):
    return a ** 2 * math.pi
def sphere_volume(a):
    return a ** 3 * 4.0/3 * math.pi
def avg_volume(a, b):
    c = a/2
    d = b/2
    return (sphere_volume(c) + sphere_volume(d)) / 2
def area(a, b, c):
    p = (a + b + c)/2.0
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def right_align(word):
    s = 80 - len(word)
    return s*" " + word
def center(word):
    s = 80 - len(word)
    x = s/2
    return x*" " + word + x*" "
def msg_box(word):
    s = len(word)
    return "+--" + s*"-" + "--+\n" + "|  " + word + "  |\n" + "+--" + s*"-" + "--+"
fnc1 = add(1, 2)
fnc2 = add(3, 4)
fnc3 = sub(7, 4)
fnc4 = sub(12, 4)
fnc5 = mul(15, 2)
fnc6 = mul(54, 6)
fnc7 = div(42, 6)
fnc8 = div(69, 3)
fnc9 = hours_from_seconds(46800)
fnc10 = hours_from_seconds(248400)
fnc11 = circle_area(3)
fnc12 = circle_area(43)
fnc13 = sphere_volume(2)
fnc14 = sphere_volume(4)
fnc15 = avg_volume(6, 8)
fnc16 = avg_volume(7, 9)
fnc17 = area(2, 3, 4)
fnc18 = area(5, 7, 9)
fnc19 = right_align("This is so tedious.")
fnc20 = right_align("This takes soo long...")
fnc21 = center("Computer")
fnc22 = center("Science")
fnc23 = msg_box("CATS")
fnc24 = msg_box("Grumpy cat")
print msg_box("The result of add is " + str(fnc1))
print msg_box("The result of add is " + str(fnc2))
print msg_box("The result of sub is " + str(fnc3))
print msg_box("The result of sub is " + str(fnc4))
print msg_box("The result of mul is " + str(fnc5))
print msg_box("The result of mul is " + str(fnc6))
print msg_box("The result of div is " + str(fnc7))
print msg_box("The result of div is " + str(fnc8))
print msg_box("The result of hours_from_seconds is " + str(fnc9))
print msg_box("The result of hours_from_seconds is " + str(fnc10))
print msg_box("The result of circle_area is " + str(fnc11))
print msg_box("The result of circle_area is " + str(fnc12))
print msg_box("The result of sphere_volume is " + str(fnc13))
print msg_box("The result of sphere_volume is " + str(fnc14))
print msg_box("The result of avg_volume is " + str(fnc15))
print msg_box("The result of avg_volume is " + str(fnc16))
print msg_box("The result of area is " + str(fnc17))
print msg_box("The result of area is " + str(fnc18))
print fnc19 + "\nis right aligned"
print fnc20 + "\nis right aligned"
print fnc21 + "\nis centered"
print fnc22 + "\nis centered"
print fnc23 + " is in a message box"
print fnc24 + " is in a message box"
