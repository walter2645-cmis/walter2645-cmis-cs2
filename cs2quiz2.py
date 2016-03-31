#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 1 == 1
#b) 2 >= 3
#c) "Hello" != "bye"
#
#2) What does 'return' do?
# returns some form of output from a function
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) clearly separates different parts of code
#b) tells us what code is in what function
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36
#problem1_b)negative the square root of 3
#problem1_c) 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 24
#problem4_b) 6
#problem4_c) 1.5
#problem4_d) 5
#

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
