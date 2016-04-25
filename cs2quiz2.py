#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 1 == 1
#b) 2 >= 3
#c) "Hello" != "bye"
# 3 points
#2) What does 'return' do?
# returns some form of output from a function
# 0 points
#
#
#3) What are 2 ways indentation is important in python code?
#a) clearly separates different parts of code
#b) tells us what code is in what function
# 1 points
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36
#problem1_b)negative the square root of 3
#problem1_c) 0
#problem1_d) -5
# 4 points
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
# 3 points
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
# 4 points
#problem4_a) 24
#problem4_b) 6
#problem4_c) 1.5
#problem4_d) 5
# 4 points

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def compare(a, b, c):
    if a > b and a > c and b != c:
        return a
    elif b > a and b > c and a != c:
        return b
    elif c > a and c > b and a != b:
        return c
    else:
        return "Wrong"
def output1(num):
    out = "The largest number was " + str(num)
    return out
def output2():
    out = "You didnt follow diections"
    return out
def main():
    #Input Section
    a = float(raw_input("Type in 3 different numbers (decimals are OK!)\nA: "))
    b = float(raw_input("B: "))
    c = float(raw_input("C: "))

    #Processing
    compareres = compare(a, b, c)
    if compareres == "Wrong":
        res = output2()
    elif compareres == float(compareres):
        res = output1(compareres)

    #Output Section
    print res
main()

# +1 correct function headers (ALL MUST BE CORRECT) +1
# +1 correctly structured script: 
#	 (main function defined, process functions defined, process functions called +1
#     in main, calls main)
# +1 use if...elif...else or an equivalent structure +1
# +1 uses a boolean expression to test numbers +1
# +1 CORRECTLY determines and returns largest number +1
# +1 uses if...else or an equivalent structure +1
# +1 uses a boolean expression to test equality +1
# +1 CORRECTLY determines and returns if the numbers are all different +1
# +1 gets and converts 3 values correctly +1
# +1 uses conditional to give feedback if numbers are not all different +1
