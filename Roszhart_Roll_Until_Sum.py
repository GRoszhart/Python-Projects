import random

def Roll():
    return random.randrange(1,7)

def Main():
    print("Welcome to the Roll Until Sum Program!")
    print()
    print("This program rolls two 6 sided dice until their sum is a certain target value.")
    print()
    while True:
        TargetValue = int(input("What is your desired sum to roll for? "))
        if (TargetValue < 2 or TargetValue > 12):
            print("It is impossible to roll that value.")
        else:
            break
    print()
    NumberOfRolls = 0
    while True:
        DieOne = Roll()
        DieTwo = Roll()
        DiceSum = DieOne + DieTwo
        print("Roll: {} and {}, sum is {}".format(DieOne,DieTwo,DiceSum))
        NumberOfRolls = NumberOfRolls + 1
        
        if DiceSum == TargetValue:
            break;
    print()
    print("We rolled your value in {} rolls!".format(NumberOfRolls))
    print()
    print("Thanks for using my dice roller program!")
    
Main()