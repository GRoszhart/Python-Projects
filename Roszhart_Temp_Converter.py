for tempConversions in range(3):
    inputFahrenheitString = input("Enter your temperature in degrees Fahrenheit: ")
    tempF = float(inputFahrenheitString)
    tempC = (tempF - 32) * (5/9)
    print ("The temperature in degrees Celsius is ", tempC)