#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# assigning values, function calls to a variable
#
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that perform some calculation and may return an output
#
#
#3 1pt) What does the keyword "return" do?
# returns some form of output from a function
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean: True, False
#	2: string: "ASDASD", "sooosad"
#	3: float: 1.23, 14264.80124
#	4: integer: 314, 0
#	5: tuple: True, "SDA", 12.456, 87
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# a function definition defines what the function does and a function call calls the function to do what it was defined to do.
# the main difference between the two is the definition has a ":" after it while the function call does not
# a function must me defined before it can be called
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input: user inputs something
#	2: Processing/computation: computer does something with the input
#	3: Output: computer returns some form of output
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
import math
def diameterfromarea(x):
    return math.sqrt(x/math.pi)*2
def output(c1, c2, c3, total):
    out = """
Circle  Diameter
c1      {}
c2      {}
c3      {}
Totals  {}
""".format(c1, c2, c3, total)
    return out
def main():
    #Input Section
    a = float(raw_input("Area of C1: "))
    b = float(raw_input("Area of C2: "))
    c = float(raw_input("Area of C3: "))

    #Processings
    c1 = diameterfromarea(a)
    c2 = diameterfromarea(b)
    c3 = diameterfromarea(c)
    total = c1 + c2 + c3

    #Output Section
    res = output(c1, c2, c3, total)
    print res
main()
