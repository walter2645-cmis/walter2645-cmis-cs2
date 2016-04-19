import math
def average():
    amoutofnumbers = 0
    total = 0
    n0 = float(raw_input("n0: "))
    if 0 <= n0 < 10:
        amoutofnumbers += 1
        total += n0
    else:
        print str(n0) + " is out of range."
    n1 = float(raw_input("n1: "))
    if 0 <= n1 < 10:
        amoutofnumbers += 1
        total += n1
    else:
        print str(n1) + " is out of range."
    n2 = float(raw_input("n2: "))
    if 0 <= n2 < 10:
        amoutofnumbers += 1
        total += n2
    else:
        print str(n2) + " is out of range."
    n3 = float(raw_input("n3: "))
    if 0 <= n3 < 10:
        amoutofnumbers += 1
        total += n3
    else:
        print str(n3) + " is out of range."
    n4 = float(raw_input("n4: "))
    if 0 <= n4 < 10:
        amoutofnumbers += 1
        total += n4
    else:
        print str(n4) + " is out of range."
    return total / amoutofnumbers
def evenorodd(num):
    if num/2.0 == num/2:
        return "even"
    else:
        return "odd"
def output(fltavg, intavg, numberis):
    out = """The average is {}
The integer part of the average is {}.
The integer part is {}.""".format(fltavg, intavg, numberis)
    return out
def main():
    print "\nThis program will ask you for 5 integer or float values.\nIt will calculate the average of all values from 0 inclusive to 10 exclusive.\nIt will print out whether the resulting average is even or odd.\n"
    #Input    
    fltavg = average()
    #Processing    
    intavg = int(fltavg)
    numberis = evenorodd(intavg)
    #Output    
    res = output(fltavg, intavg, numberis)
    print res
main()
