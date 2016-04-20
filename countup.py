def countup(start, stop):
    if start > stop:
        print "Done!"
    else:
        print start
        countup(start+1, stop)
def main():
    countup(0, 13)
main()
