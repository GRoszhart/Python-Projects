print("Hello and welcome to my Golf Club Helper!")
print("Please tell me about your situtation, and I will recommend your club!")
print()
ShotOnGreen = input("Did your previous shot land on the green (y/n)? ")
print()
if ShotOnGreen.lower() == 'y' or ShotOnGreen.lower() == 'yes':
    print("I suggest using the Putter!")
else:
    YardsFromHole = int(input("How far, in yards, did your previous shot land from the hole? "))
    print()
    if YardsFromHole >= 200:
        print("I suggest using your Driver, or lowest number Wood if not on tee box!")
    elif YardsFromHole >= 140 and YardsFromHole < 200:
        print("I suggest using your 5-Iron!")
    elif YardsFromHole >= 100 and YardsFromHole < 140:
        print("I suggest using your 9-Iron!")
    else:
        print("I suggest using your Wedge!")
print()
print("Thanks for using my Golf Club Helper!")