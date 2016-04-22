def adder(inp, total):
    if inp == "":
        return total
    else:
        total += float(inp)
        inp = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(inp, total)
def main():
    res = adder(0, 0)
    print "The sum is " + str(res)
main()
