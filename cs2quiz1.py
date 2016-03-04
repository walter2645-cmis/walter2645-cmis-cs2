# 13.5 pts of 15 for terminology
# 20 pts of 25 for programming
#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# assigning values, function calls to a variable
# 1 pt right answer
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that perform some calculation and may return an output
# 3 pts right answer
#
#3 1pt) What does the keyword "return" do?
# returns some form of output from a function
# 1 pt right answer
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean: True, False
#	2: string: "ASDASD", "sooosad"
#	3: float: 1.23, 14264.80124
#	4: integer: 314, 0
#	5: tuple: True, "SDA", 12.456, 87
# 4pts, missed parenthesis on tuple
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# a function definition defines what the function does and a function call calls the function to do what it was defined to do.
# the main difference between the two is the definition has a ":" after it while the function call does not
# a function must me defined before it can be called
#  1.5 pts, mostly right answer, missed function name
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input: user inputs something
#	2: Processing/computation: computer does something with the input
#	3: Output: computer returns some form of output
# 3pts right answer
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
#1 pt for header line 1 pt correct
#3 pt for correct formula 3 pt correct
#1 pt for return value 1 pt correct
#1 pt for parameter name 0 pt put x instead of area
#1 pt for function name 1 pt correct
def diameterfromarea(x):
    return math.sqrt(x/math.pi)*2
#1pt for header line 1 pt correct
#1pt for parameter names 1 pt correct
#1pt for return value 1 pt correct
#1pt for correct output format 1 pt correct
#3pt for correct use of format function 3 pts correct
def output(c1, c2, c3, total):
    out = """
Circle  Diameter
c1      {}
c2      {}
c3      {}
Totals  {}
""".format(c1, c2, c3, total)
    return out
#1pt header line 1 pt correct
#1pt getting input 1 pt got input
#1pt converting input 1 pt converted input
#1pt for calling output function 1 pt called output
#2pt for correct diameter formula 2 pts correct
#1pt for variable names 0 pt used single letter variable names
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
#1pt for calling main 1 pt main called
main()
#1pt explanatory comments 1 pt added explanatory comments
#1pt code format 1 pt code format correct
#1pt script runs without errors 1 pt script runs no errors
