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
    return a * a * math.pi
def sphere_volume(a):
    return a * a * a * 4.0/3 * math.pi
def avg_volume(a, b):
    c = a/2
    d = b/2
    return (c * c * c * 4.0/3 * math.pi + d * d * d * 4.0/3 * math.pi) / 2
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
