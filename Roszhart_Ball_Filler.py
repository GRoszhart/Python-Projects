import math
bowlingBallCount = int (input ("How many bowling balls will be manufactured? "))
ballDiameter = float (input ("What is the ball diameter in inches? "))
coreVolume = int (input ("What is the core volume in inches cubed? "))
ballVolume = bowlingBallCount * ((4/3) * math.pi * (ballDiameter / 2) ** 3 - coreVolume)
print ("You will need ", ballVolume, "inches of ball filler.")