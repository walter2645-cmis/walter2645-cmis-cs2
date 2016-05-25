#Section 1: Terminology
# 1) What is a recursive function?
# a function that calls itself within it.
# 1 point
#
# 2) What happens if there is no base case defined in a recursive function?
# it recurses indefinetly until it reaches the limit set by the computer
# 1 point
#
# 3) What is the first thing to consider when designing a recursive function?
# the base case
# 1 point
#
# 4) How do we put data into a function call?
# in an argument
# 1 point
# 
# 5) How do we get data out of a function call?
# return from the function
# 1 point
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1
# 3 points
#b1 = 2
#b2 = 1 (wrong)
#b3 = 5 (wrong)
# 1 point
#c1 = -2
#c2 = 4
#c3 = 45
# 3 points
#d1 = 4 (wrong)
#d2 = 9 (wrong)
#d3 = 2 (wrong)
#0 points
#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.
# +2 base case is present (MUST BE LABELED) 2 points
# +2 recursive case is present (MUST BE LABELED) 2 points
# +1 base case returns sum/ct (or equivalent) 1 point
# +2 recursive case filters even numbers 2 points
# +1 recursive case increments sum and ct correctly 1 point
# +1 recursive case returns correct recursive call 1 point
# +1 main function present AND called  1 point
def averageofodds(avg, num):
    inp = raw_input("Next: ")
#BASE CASE
    if inp == "":
        if avg == 0:
            return "nothing because you either did not type in any numbers or you only typed in even numbers"
        else:
            return float(num) / avg
#RECURSIVE CASE(S)
    elif float(inp) % 2 == 1:
        avg += 1
        num += int(inp)
        return averageofodds(avg, num)
    else:
        return averageofodds(avg, num)
def main():
    res = averageofodds(0, 0)
    print "The average of your odd numbers was " + str(res) + "."
main()
