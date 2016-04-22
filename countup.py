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
def main():
    countdown(10)
    countup(0)
    countdownfrom(10, 3)
    countupfrom(0, 13)
main()
