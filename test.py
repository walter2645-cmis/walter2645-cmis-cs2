def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
def text_comp():
    a = raw_input("Type anything:\n")
    b = raw_input("Type exactly what you typed just now again, please:\n")
    if a == b:
        return "Congratulations! You followed the instructions correctly!"
    else:
        return "sdfk"
def num_comp():
    a = float(raw_input("Type a number:\n"))
    b = float(raw_input("Type another number:\n"))
    if a == b:
        return "The numbers are equal."
    elif a > b:
        return "The first number is greater than the second number."
    elif a < b:
        return "The first number is less than the second number."
print num_comp()
