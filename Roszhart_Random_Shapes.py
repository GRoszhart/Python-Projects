import random

def getColors(minRed,minGreen,minBlue,rgbRange):
    Red = random.randrange(max(minRed,0),min(minRed+rgbRange,255))
    Green = random.randrange(max(minGreen,0),min(minGreen+rgbRange,255))
    Blue = random.randrange(max(minBlue,0),min(minBlue+rgbRange,255))
    return str(Red) + ", " + str(Green) + ", " + str(Blue)

def getRectangleDimensions(maxHeight,maxWidth):
    upperLeftX = random.randrange(0,maxWidth)
    upperLeftY = random.randrange(0,maxHeight)
    lowerRightX = random.randrange(0,maxWidth)
    lowerRightY = random.randrange(0,maxHeight)
    return "Rectangle: " + str(upperLeftX) + ", " + str(upperLeftY) + "; " + str(lowerRightX) + ", " + str(lowerRightY)

def getCircleDimensions(maxHeight,maxWidth):
    centerX = random.randrange(0,maxWidth)
    centerY = random.randrange(0,maxHeight)
    maxRadiusX = min(maxWidth-centerX,centerX-0)
    maxRadiusY = min(maxHeight-centerY,centerY-0)
    circleRadius = random.randrange(0, min(maxRadiusX,maxRadiusY))
    return "Circle: " + str(centerX) + ", " + str(centerY) + "; " + str(circleRadius)

def main():
    windowHeight = 500
    windowWidth = 500
    minRed = random.randrange(0,205)
    minGreen = random.randrange(0,205)
    minBlue = random.randrange(0,205)
    rgbRange = 50
    shapesList = ["Rectangle","Circle"]
    
    print("Welcome to the Random Shapes Program!")
    print()
    outputFileName = input("Enter the drawing file name to create: ")
    print()
    numberOfShapes = int(input("Enter the number of shapes to make: "))
    print()
    f = open(outputFileName,"w")
    print("Generated Shapes: ")
    print()
    for indx in range(numberOfShapes):
        shapeRgb = getColors(minRed,minGreen,minBlue,rgbRange)
        shapeType = random.choice(shapesList)
        
        if shapeType == "Rectangle":
            shapeDimensions = getRectangleDimensions(windowHeight,windowWidth)
        elif shapeType == "Circle":
            shapeDimensions = getCircleDimensions(windowHeight,windowWidth)
        
        f.write(shapeDimensions + "; " + shapeRgb + "\n")
        print(shapeDimensions + "; " + shapeRgb)
        
    f.close()
    print()
    print("Thank you for using my Random Shapes Program!")

main()