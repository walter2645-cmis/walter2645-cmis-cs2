def counter(x):
    if x > 0:
        while x >= 0:
            print x
            x -= 1
    else:
        while x <= 0:
            print x
            x += 1
def counter2(x):
    while x >= 0:
        print x
        x -= 1
    while x <= 0:
        print x
        x += 1
#def sequence(n):
#   while n != 1:
#        print n,
#        if n%2 == 0:        # n is even
#            n = n/2
#        else:               # n is odd
#            n = n*3+1
#sequence(21)
def countfromto(x, y):
    while x < y:
        print x
        x += 1
    while x >= y:
        print x
        x -= 1
#countfromto(-10, 10)
#countfromto(12, 3)
def sumofodds(n):
    total = 0
    while n < 0:
        if n % 2 == 1:
            total += n
            n += 1
        else:
            n += 1
    while n > 0:
        if n % 2 == 1:
            total += n
            n -= 1
        else:
            n -= 1
    return total
#print sumofodds(10)
#print sumofodds(-35)
def grid(w, h):
    row = ""
    stasis = w
    while h > 0:
        w = stasis
        while w > 0:
            row += "."
            w -= 1
        row += "\n"
        h -= 1
    return row
print grid(10, 10)
print grid(4, 5)



























