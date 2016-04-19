import math
def average(attemptcount, total, amountofnumbers):
    num = float(raw_input("n" + str(attemptcount) + ": "))
    if attemptcount == 4:
        return total / amountofnumbers
    elif 0 <= num < 10:
        attemptcount += 1
        amountofnumbers += 1
        total += num
        return average(attemptcount, total, amountofnumbers)
    else:
        attemptcount += 1
        print str(num) + " is out of range."
        return average(attemptcount, total, amountofnumbers)
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
    startvalue = 0
    fltavg = average(startvalue, startvalue, startvalue)
    #Processing
    intavg = int(fltavg)
    numberis = evenorodd(intavg)
    #Output
    res = output(fltavg, intavg, numberis)
    print res
main()
