def countdown(n):
    if n <= 0:
        print "Blastoff!"
    else: 
        print n
        countdown(n-1)
def countup(n):
    if n >= 10:
        print "BOOM!"
    else:
        print n
        countup(n+1)
def countdownfrom(start, stop):
    if start < stop:
        print "Done!"
    else:
        print start
        countdownfrom(start-1, stop)
def countupfrom(start, stop):
    if start > stop:
        print "Done!"
    else:
        print start
        countupfrom(start+1, stop)
def counts():
    countdown(10)
    countup(0)
    countdownfrom(10, 3)
    countupfrom(0, 13)
    pass
def adder(inp, total):
    if inp == "":
        return total
    else:
        total += float(inp)
        inp = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(inp, total)
def adderout():
    res = adder(0, 0)
    print "The sum is " + str(res)
def biggest(inp, num):
    if inp == "" or num == "":
        return num
    elif num == None:
        num = raw_input("Next number: ")
        return biggest(num, num)
    elif float(inp) > num:
        num = float(inp)
        inp = raw_input("Next number: ")
        return biggest(inp, num)
    else:
        inp = raw_input("Next number: ")
        return biggest(inp, num)
def biggestout():
    res = biggest(0, None)
    print "The biggest number is " + str(res)
biggestout()
