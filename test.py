name = raw_input("What is your name?\n")
a = int(raw_input("Type a number:\n"))
b = int(raw_input("Type another number:\n"))
c = a + b
abc = """
Greetings {}.
Did you know:
{} + {} = {}
""".format(name, a, b, c)
print abc
