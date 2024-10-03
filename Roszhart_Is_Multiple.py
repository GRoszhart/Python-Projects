x = int(input("Enter a number (x): "))
y = int(input("Enter a number (y): "))
moduloResult = x % y
if (moduloResult == 0):
    print("True, (x) is a multiple of (y)")
else:
    print("False, (x) is NOT a multiple of (y)")