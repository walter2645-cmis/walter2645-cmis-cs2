#You are playing an antique RPG game.
#You are asked for your age. returns a message depending on whether player is over 18.
#You are asked if you want to read an introduction to the game.
#If you choose yes, it will print out a brief introduction.
#
#
def legalage(legal):
    if legal == "no":
        return "You will be psychologically scarred if you continue."
def main():
    #Input
    legal = raw_input("Greetings, Traveler.\nAre you over the age of 18?(yes/no)\n")
    print legalage(legal)
    #Processing
    
    #Output
main()
